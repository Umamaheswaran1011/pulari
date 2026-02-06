from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 
import json
from .models import Product, Order

# ==========================================
#              PUBLIC PAGES
# ==========================================

# 1. Home Page View
def index(request):
    items = Product.objects.all()
    return render(request, 'intex.html', {'items': items})

# 2. Product Page View (Updated with Search & Filter)
def product_page(request):
    # Fetch all items initially
    items = Product.objects.all()
    
    # Get list of unique categories for the filter buttons
    categories = Product.objects.values_list('category', flat=True).distinct()

    # Search Logic (Filter by name)
    query = request.GET.get('q')
    if query:
        items = items.filter(name__icontains=query)

    # Category Filter Logic (Filter by category)
    category_filter = request.GET.get('category')
    if category_filter and category_filter != 'All':
        items = items.filter(category=category_filter)

    context = {
        'items': items,
        'categories': categories,
        'active_category': category_filter,
        'search_query': query
    }
    return render(request, 'product_page.html', context)

# 3. Order Logic (With Stock Reduction & Email)
@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            p_name = data.get('product')
            qty = int(data.get('quantity'))

            # -----------------------------------------------
            # 1. STOCK CHECK & REDUCTION LOGIC
            # -----------------------------------------------
            product_obj = None
            try:
                # Check if product exists in Database
                product_obj = Product.objects.get(name=p_name)
            except Product.DoesNotExist:
                # If product is not found (e.g. "Other Inquiry"), skip stock reduction
                pass

            if product_obj:
                if product_obj.stock >= qty:
                    # Reduce stock if available
                    product_obj.stock = product_obj.stock - qty
                    product_obj.save() # Update Database
                else:
                    # Return error if insufficient stock
                    return JsonResponse({
                        'status': 'error', 
                        'message': f'Sorry! Only {product_obj.stock} items left in stock.'
                    }, status=400)
            
            # -----------------------------------------------
            # 2. SAVE ORDER TO DATABASE
            # -----------------------------------------------
            order = Order.objects.create(
                customer_name=data.get('name'), 
                phone=data.get('phone'),
                email=data.get('email', ''),   
                product=p_name,
                quantity=qty,
                message=data.get('message', '')
            )

            # -----------------------------------------------
            # 3. EMAIL SENDING LOGIC
            # -----------------------------------------------
            email_errors = []
            
            try:
                # A. Email to Customer
                if data.get('email'):
                    try:
                        send_mail(
                            f"Order Confirmation - Pulari Pipes (Order #{order.id})",
                            f"Hello {data.get('name')},\n\nThank you for ordering!\nProduct: {p_name}\nQty: {qty}\n\nWe will contact you shortly.",
                            settings.EMAIL_HOST_USER,
                            [data.get('email')],
                            fail_silently=False,
                        )
                        print(f"✓ Customer email sent to {data.get('email')}")
                    except Exception as e:
                        error_msg = f"Customer Email Failed: {str(e)}"
                        print(f"✗ {error_msg}")
                        email_errors.append(error_msg)
            except Exception as e:
                error_msg = f"Customer Email Failed: {str(e)}"
                print(f"✗ {error_msg}")
                email_errors.append(error_msg)

            try:
                # B. Email to Admin
                remaining_stock = product_obj.stock if product_obj else 'N/A'
                try:
                    send_mail(
                        f"New Order Alert! (#{order.id})",
                        f"New Order Received!\n\nName: {data.get('name')}\nPhone: {data.get('phone')}\nProduct: {p_name}\nQty: {qty}\nStock Remaining: {remaining_stock}",
                        settings.EMAIL_HOST_USER,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                    )
                    print(f"✓ Admin email sent to {settings.EMAIL_HOST_USER}")
                except Exception as e:
                    error_msg = f"Admin Email Failed: {str(e)}"
                    print(f"✗ {error_msg}")
                    email_errors.append(error_msg)
            except Exception as e:
                error_msg = f"Admin Email Failed: {str(e)}"
                print(f"✗ {error_msg}")
                email_errors.append(error_msg)
            
            # Log all email errors
            if email_errors:
                print(f"\n⚠️ EMAIL ERRORS:\n" + "\n".join(email_errors))
            else:
                print("✓ All emails sent successfully!")

            return JsonResponse({'status': 'success', 'order_id': order.id})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Only POST allowed'}, status=405)


# ==========================================
#           ADMIN DASHBOARD VIEWS
# ==========================================

# 4. Admin Dashboard
@login_required(login_url='admin:login')
def admin_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all().order_by('-created_at')
    
    p_names = []
    p_stocks = []
    low_stock_count = 0
    
    for p in products:
        p_names.append(p.name)
        p_stocks.append(p.stock)
        
        if p.stock < 5:
            p.status_color = 'red'
            p.status_text = 'Out of Stock'
            low_stock_count += 1
        elif p.stock < 10:
            p.status_color = 'orange'
            p.status_text = 'Low Stock'
            low_stock_count += 1
        else:
            p.status_color = 'green'
            p.status_text = 'In Stock'

    context = {
        'products': products,
        'orders': orders,
        'total_products': products.count(),
        'total_orders': orders.count(), 
        'low_stock_count': low_stock_count,
        'p_names': p_names,
        'p_stocks': p_stocks,
    }
    return render(request, 'admin_dashboard.html', context)


# 5. Add Product
@login_required(login_url='admin:login')
@require_http_methods(["GET", "POST"])
def add_product(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            category = request.POST.get('category')
            price = request.POST.get('price')
            stock = request.POST.get('stock')
            description = request.POST.get('description')
            image = request.FILES.get('image') if request.FILES else None
            
            if not all([name, category, price, stock, description]):
                return render(request, 'add_product.html', {'error': 'All fields are required!'})
            
            Product.objects.create(
                name=name, 
                category=category, 
                price=float(price),
                stock=int(stock), 
                description=description, 
                image=image
            )
            
            messages.success(request, "Product added successfully!")
            return redirect('admin_dashboard')
            
        except ValueError:
            return render(request, 'add_product.html', {'error': 'Price/Stock must be numbers!'})
        except Exception as e:
            return render(request, 'add_product.html', {'error': f'Error: {str(e)}'})
    
    return render(request, 'add_product.html')


# 6. Edit Product
@login_required(login_url='admin:login')
@require_http_methods(["GET", "POST"])
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        try:
            product.name = request.POST.get('name', product.name)
            product.category = request.POST.get('category', product.category)
            product.price = float(request.POST.get('price', product.price))
            product.stock = int(request.POST.get('stock', product.stock))
            product.description = request.POST.get('description', product.description)
            
            if request.FILES.get('image'):
                product.image = request.FILES['image']
            
            product.save()
            messages.success(request, "Product updated successfully!")
            return redirect('admin_dashboard')
            
        except ValueError:
            return render(request, 'edit_product.html', {'product': product, 'error': 'Invalid Input'})
    
    return render(request, 'edit_product.html', {'product': product})


# 7. Delete Product
@login_required(login_url='admin:login')
@require_http_methods(["POST"])
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)