# Admin Dashboard - Visual Guide

## 📍 Navigation Map

```
http://localhost:8000/
│
├─→ /admin/  [LOGIN REQUIRED]
│   └─→ Django default admin (for superuser management)
│
├─→ /admin-dashboard/  [LOGIN REQUIRED]
│   ├─→ View all products
│   ├─→ See stock status
│   ├─→ "Add New Product" button ──→ /admin/product/add/
│   ├─→ Edit button (pencil) ──→ /admin/product/<id>/edit/
│   └─→ Delete button (trash) ──→ POST /admin/product/<id>/delete/
│
└─→ /products/ [NO LOGIN NEEDED]
    ├─→ / (Home page with products)
    └─→ /product_page/ (Product listing page)
```

---

## 🎨 User Interface Layout

### Dashboard Page
```
┌─────────────────────────────────────────────────────┐
│ ADMIN DASHBOARD                          [Logout]   │ ← Header
├─────────────────────────────────────────────────────┤
│                                                     │
│ ┌──────────────┐  ┌──────────────┐               │
│ │ Total:  X    │  │ Low Stock: Y  │               │ ← Stats
│ │ Products     │  │ Items        │               │
│ └──────────────┘  └──────────────┘               │
│                                                     │
│ Products Inventory                  [+ Add New]    │ ← Title & Button
│                                                     │
│ ┌─────────────────────────────────────────────────┐ │
│ │ ID  │ Name   │ Category │ Price │ Stock │ ... │ │ ← Table
│ ├─────────────────────────────────────────────────┤ │
│ │ 1   │ Pipe   │ PVC      │ ₹100  │ 50    │ ✏️ 🗑️ │ │
│ │ 2   │ Pipe   │ CPVC     │ ₹150  │ 5  ⚠️ │ ✏️ 🗑️ │ │
│ │ 3   │ Pipe   │ Metal    │ ₹200  │ 2  ❌ │ ✏️ 🗑️ │ │
│ └─────────────────────────────────────────────────┘ │
│                                                     │
│ Stock Alerts                                        │
│ ┌─────────────────────────────────────────────────┐ │
│ │ ⚠️ Low Stock Items - Reorder Recommended!       │ │
│ │ • Product Name (5 remaining)                    │ │
│ │ • Other Product (8 remaining)                   │ │
│ └─────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

---

### Add Product Form
```
┌─────────────────────────────────────────────────────┐
│ ➕ ADD NEW PRODUCT              [← Back to Dashboard]│ ← Header
├─────────────────────────────────────────────────────┤
│                                                     │
│ Form:                                               │
│ ┌─────────────────────────────────────────────────┐ │
│ │ Product Name *                                  │ │
│ │ [___________________________________]           │ │
│ │                                                 │ │
│ │ Category * │ Price (₹) *                       │ │
│ │ [Dropdown] │ [____________]                     │ │
│ │                                                 │ │
│ │ Stock Quantity * │ Product Image               │ │
│ │ [____________]   │ [Choose File]               │ │
│ │                                                 │ │
│ │ Description *                                   │ │
│ │ [_____________________________________]         │ │
│ │ [_____________________________________]         │ │
│ │ [_____________________________________]         │ │
│ │                                                 │ │
│ │ [💾 Add Product] [❌ Cancel]                    │ │
│ └─────────────────────────────────────────────────┘ │
│                                                     │
│ Tips:                                               │
│ • Use clear, descriptive product names             │ │
│ • Select appropriate category                      │ │
│ • Include specifications in description            │ │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### Delete Confirmation Modal
```
┌─────────────────────────────┐
│ ⚠️ Confirm Delete        [×] │
├─────────────────────────────┤
│                             │
│ Are you sure you want to    │
│ delete "Product Name"?      │
│                             │
│ ⚠️ This action cannot be    │
│    undone.                  │
│                             │
│ [Cancel]  [Delete Product]  │
│                             │
└─────────────────────────────┘
```

---

## 🎯 Feature Highlight Zones

### Stock Status Indicators
```
✅ IN STOCK (Green)         Product has 10+ units
⚠️  LOW STOCK (Yellow)       Product has 5-9 units  
❌ OUT OF STOCK (Red)       Product has <5 units
```

### Action Buttons
```
🟢 Primary (Green)     - Add, Save, Create
🔵 Secondary (Blue)    - Edit, Update
🔴 Danger (Red)        - Delete
⚪ Neutral (Gray)      - Cancel, Back
```

---

## 🔄 Data Flow Diagram

### Adding a Product
```
User visits /admin/product/add/
         ↓
HTML Form Displayed
         ↓
User fills form (name, category, price, stock, image, description)
         ↓
User clicks "Add Product"
         ↓
Form data sent via POST
         ↓
Django validates data
         ↓
If valid → Save to database
          ↓
          Redirect to /admin-dashboard/
          ↓
          New product shows in table
          
If invalid → Show error message
            ↓
            User corrects and retries
```

### Deleting a Product
```
User clicks delete button
         ↓
Confirmation modal appears
         ↓
User clicks "Delete Product"
         ↓
AJAX request sent
         ↓
Django checks for pending orders
         ↓
If orders pending → Return error
                   ↓
                   Show error toast
                   
If no orders → Delete from database
              ↓
              Return success
              ↓
              Show success toast
              ↓
              Reload dashboard
```

---

## 📊 Database Table Structure

### Product Table
```
┌────────┬──────────────┬──────────┬────────┬───────┬──────────────┬────────┐
│   ID   │    NAME      │ CATEGORY │ PRICE  │ STOCK │ DESCRIPTION  │ IMAGE  │
├────────┼──────────────┼──────────┼────────┼───────┼──────────────┼────────┤
│   1    │ PVC Pipe 1"  │   PVC    │ 100.00 │  50   │ Standard... │ ...jpg │
│   2    │ CPVC Pipe 2" │  CPVC    │ 150.50 │   5   │ High... │ ...jpg │
│   3    │ Metal Pipe   │  Metal   │ 200.00 │   2   │ Durable...   │ ...jpg │
└────────┴──────────────┴──────────┴────────┴───────┴──────────────┴────────┘
```

### Order Table (for deletion check)
```
┌────┬──────────────┬────────┬─────────┬──────────┬────────────┬──────────────┐
│ ID │ CUSTOMER     │ PHONE  │ PRODUCT │ QUANTITY │   STATUS   │  CREATED_AT  │
├────┼──────────────┼────────┼─────────┼──────────┼────────────┼──────────────┤
│ 1  │ Customer A   │ 123456 │ Product │   10     │    new     │ 2025-01-01   │
│ 2  │ Customer B   │ 789012 │ Product │   5      │ processing │ 2025-01-02   │
│ 3  │ Customer C   │ 345678 │ Product │   2      │ completed  │ 2025-01-03   │
└────┴──────────────┴────────┴─────────┴──────────┴────────────┴──────────────┘
```

---

## 🎬 Step-by-Step Usage

### Adding Your First Product

```
1️⃣  Visit Dashboard
    URL: http://localhost:8000/admin-dashboard/

2️⃣  Click "➕ Add New Product"
    URL: http://localhost:8000/admin/product/add/

3️⃣  Fill the form:
    ┌─────────────────────────────┐
    │ Product Name: PVC Pipe 1"   │
    │ Category: PVC               │
    │ Price: 100.00               │
    │ Stock: 50                   │
    │ Image: [upload image]       │
    │ Description: Details here   │
    └─────────────────────────────┘

4️⃣  Click "💾 Add Product"

5️⃣  Redirected back to dashboard
    Product appears in table with 50 in stock ✅
```

### Editing a Product

```
1️⃣  Find product in table

2️⃣  Click ✏️ Edit icon

3️⃣  Update any field

4️⃣  Click "💾 Update Product"

5️⃣  Changes saved, dashboard refreshed ✅
```

### Deleting a Product

```
1️⃣  Find product in table

2️⃣  Click 🗑️ Delete icon

3️⃣  Modal appears asking for confirmation

4️⃣  System checks for pending orders

    IF orders pending:
    ❌ "Cannot delete! 2 pending orders exist"

    IF no orders:
    ✅ Product deleted from database

5️⃣  Dashboard reloads ✅
```

---

## 🔐 Access Control

```
        Anonymous User
              │
              ↓
        Tries to access /admin-dashboard/
              │
              ↓
        Redirected to /admin/login/
              │
              ↓
        ┌─────────────────────────┐
        │ Login Page              │
        │ Username: [________]    │
        │ Password: [________]    │
        │ [Login]                 │
        └─────────────────────────┘
              │
              ↓
        ┌─────────────────────────┐
        │ Is superuser?           │
        │                         │
        │ YES ─→ ✅ Access granted
        │ NO  ─→ ❌ Permission denied
        └─────────────────────────┘
```

---

## 📱 Responsive Behavior

### Desktop View (1200px+)
```
Full table with all columns visible
Side-by-side form fields
Normal button sizes
```

### Tablet View (768px-1199px)
```
Table with horizontal scroll
Stacked form fields (2 per row)
Adjusted spacing
```

### Mobile View (<768px)
```
Scrollable table
Single column form fields
Large touch-friendly buttons
Stacked navigation
```

---

## 🎨 Color Reference

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Green | #4CAF50 | Main actions, In Stock |
| Secondary Blue | #2196F3 | Edit actions, Secondary |
| Danger Red | #f44336 | Delete actions, Out of Stock |
| Warning Orange | #ff9800 | Low Stock alerts |
| Success Green | #4CAF50 | In Stock badges |
| Light Gray | #f5f5f5 | Background, Hover states |
| Border Gray | #ddd | Borders, Separators |
| Dark Text | #333 | Main text |
| Light Text | #666 | Secondary text |

---

## 💬 Message Examples

### Success Messages
```
✅ Product added successfully!
✅ Product updated successfully!  
✅ Product deleted successfully!
```

### Error Messages
```
❌ Cannot delete! 2 pending orders exist.
❌ Price must be a number!
❌ Stock must be an integer!
❌ All fields are required!
❌ Error: Something went wrong. Please try again.
```

---

**This visual guide helps you understand how the admin panel is laid out and how data flows through the system.**
