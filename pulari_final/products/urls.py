from django.urls import path
from . import views

urlpatterns = [
    # --- Public Pages ---
    path('', views.index, name='home'),
    path('product_page/', views.product_page, name='product_page'),
    path('orders/create/', views.create_order, name='create_order'),
    
    # --- Email Verification URLs ---
    path('verify-email/', views.send_verification_email, name='send_verification_email'),
    path('verify-create-order/', views.verify_and_create_order, name='verify_create_order'),

    # --- Admin Dashboard URLs ---
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/product/add/', views.add_product, name='add_product'),
    
    # Edit & Delete (ID logic sariya iruku)
    path('admin/product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('admin/product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
]