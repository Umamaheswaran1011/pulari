from django.contrib import admin
from django.urls import path, include
from django.conf import settings              
from django.conf.urls.static import static    
from products import views  # *** 1. இதை புதிதாகச் சேர்க்கவும் (Import Views) ***

urlpatterns = [
    path('admin/', admin.site.urls),

    # *** 2. Admin Dashboard Path (இது இருந்தால் தான் Admin-ல் அந்த பட்டன் வேலை செய்யும்) ***
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Products app URL link
    path('', include('products.urls')), 
]

# Indha code irundhal mattum dhaan Images work aagum!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)