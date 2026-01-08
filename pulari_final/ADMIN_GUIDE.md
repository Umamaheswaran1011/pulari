# Admin Dashboard - Setup & Usage Guide

## ✅ Features Implemented

### 1. **Admin Dashboard** - `/admin-dashboard/`
   - View all products with stock information
   - Stock status badges (In Stock, Low Stock, Out of Stock)
   - Total products count
   - Low stock alerts section
   - Quick access to add, edit, and delete products

### 2. **Add Product** - `/admin/product/add/`
   - Form with validation for all fields:
     - Product Name
     - Category (PVC, CPVC, Metal, Plastic, Other)
     - Price (₹)
     - Stock Quantity
     - Product Image (optional)
     - Description (detailed)
   - Error handling for invalid inputs
   - Automatic redirect to dashboard after adding

### 3. **Edit Product** - `/admin/product/<id>/edit/`
   - Update existing product details
   - Keep or replace product image
   - Real-time stock status display
   - Validation for price and stock fields
   - Product ID display for reference

### 4. **Delete Product** - `/admin/product/<id>/delete/`
   - Delete confirmation modal
   - **Smart Logic**: Cannot delete product if there are pending orders
   - Prevents accidental deletion with confirmation popup
   - Shows error message if orders are pending
   - Toast notification on success/failure

## 🔐 Security Features

- **Login Required**: All admin pages use `@login_required` decorator
- **CSRF Protection**: All forms include CSRF token validation
- **HTTP Methods**: Proper HTTP method validation (GET/POST)
- **Data Validation**: All inputs validated before saving

## 📊 Stock Management

- **Low Stock Alert**: Products with stock < 10 are highlighted
- **Out of Stock**: Products with stock < 5 are marked as out of stock
- **Color Coding**: 
  - Green = In Stock (≥ 10 units)
  - Yellow = Low Stock (5-9 units)
  - Red = Out of Stock (< 5 units)

## 🎨 Admin Dashboard Design

- Clean, modern UI with gradient header
- Responsive design (works on mobile, tablet, desktop)
- Data tables with hover effects
- Icon-based navigation for better UX
- Toast notifications for user feedback
- Modal confirmations for destructive actions

## 🔧 API Endpoints

```
GET  /admin-dashboard/              - View all products
GET  /admin/product/add/            - Show add product form
POST /admin/product/add/            - Submit new product
GET  /admin/product/<id>/edit/      - Show edit form
POST /admin/product/<id>/edit/      - Update product
POST /admin/product/<id>/delete/    - Delete product (AJAX)
```

## 📝 Business Logic for Delete

```python
# Before deleting a product:
1. Check if product has any pending orders
2. If pending_orders exist:
   - Return error: "Cannot delete! X pending orders exist"
   - Do NOT delete the product
3. If no pending orders:
   - Delete the product
   - Show success message
   - Reload dashboard
```

## 🚀 How to Access

1. Go to Django Admin: `http://localhost:8000/admin/`
2. Create a superuser if not already created:
   ```
   python manage.py createsuperuser
   ```
3. Login with your superuser credentials
4. Access admin dashboard: `http://localhost:8000/admin-dashboard/`

## 📱 Responsive Features

- Mobile-friendly table with horizontal scroll
- Touch-friendly buttons and controls
- Optimized for all screen sizes
- Collapsible menu on mobile devices

## 🎯 Category Options

- **PVC** - PVC Pipes
- **CPVC** - CPVC Pipes
- **Metal** - Metal Pipes
- **Plastic** - Plastic Pipes
- **Other** - Other types

## 💡 Tips

1. Upload clear product images for better visibility
2. Include detailed descriptions with specifications
3. Keep stock numbers updated regularly
4. Check low stock alerts before orders come in
5. Use categories to organize products

## 🔴 Important Notes

- All admin pages require login
- Deleting a product with pending orders is not allowed
- Stock status updates automatically based on quantity
- Images are stored in `/media/pipes_images/` directory
- All forms validate data on both client and server side

---

**Version**: 1.0
**Last Updated**: December 2025
