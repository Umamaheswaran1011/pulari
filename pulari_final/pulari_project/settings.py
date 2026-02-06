"""
Django settings for pulari_project project.
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Old style path (Neenga create pannadhu)
BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Folder Paths
TEMPLATES_DIR = os.path.join(BASE_DIR2, 'templates')
STATIC_DIR = os.path.join(BASE_DIR2, 'static')
MEDIA_DIR = os.path.join(BASE_DIR2, 'media')

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-d#0#kpa1!7)2xxo%5w6u!jx!+vk)hkb+b1_68vmcq6v48!d=i@'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    # 1. JAZZMIN Added Here (MUST BE ON TOP)
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products', # Unga App
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pulari_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR], # Mele define panna variable use panrom
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'pulari_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC & MEDIA FILES (Main Changes Here) ---

STATIC_URL = '/static/'

# Idhu romba mukkiyam! Idhu illana CSS load aagadhu.
STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# --- 2. JAZZMIN SETTINGS (UPDATED WITH DASHBOARD LINK) ---
JAZZMIN_SETTINGS = {
    # Title on the browser tab
    "site_title": "Pulari Pipes Admin",

    # Title on the login screen
    "site_header": "Pulari Pipes",

    # Brand text on top left
    "site_brand": "Pulari Pipes",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Pulari Pipes Admin",

    # Copyright text at bottom
    "copyright": "Pulari Pipes Ltd",

    # Path to your Logo (Make sure static/img/logo.png exists)
    "site_logo": "img/logo.png",
    
    # Login screen logo
    "login_logo": "img/logo.png",

    # Custom CSS for Animation
    "site_logo_classes": "img-circle", 
    "custom_css": "css/admin_animation.css",

    # *** MUKKIYAM: DASHBOARD LINK INGE DHAN IRUKKU ***
    "topmenu_links": [
        # Home button
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        
        # New Dashboard Button (இதுதான் உங்கள் சார்ட் பேஜ்ஜுக்கு கூட்டி செல்லும்)
        {"name": "📊 Analytics Dashboard", "url": "admin_dashboard"}, 
        
        # View Website Button
        {"name": "View Site", "url": "home"},
    ],

    # Sidebar Icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "products.Product": "fas fa-box-open",
        "products.Order": "fas fa-shopping-cart",
    },
}

# EMAIL CONFIGURATION
# NOTE: Gmail requires an APP PASSWORD (not your regular password)
# To set up:
# 1. Go to https://myaccount.google.com/apppasswords
# 2. Generate a 16-character app password
# 3. Replace EMAIL_HOST_PASSWORD below with that password
# 4. Make sure 2-Factor Authentication is enabled on your Gmail account

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Update this with your Gmail address
EMAIL_HOST_USER = 'tndhoni2011@gmail.com' 

# IMPORTANT: Use the 16-character APP PASSWORD from Google, not your Gmail password!
# Error: If you get "Username and Password not accepted", the password below is invalid
EMAIL_HOST_PASSWORD = 'zzsnbqtmambvswug'  # This password is invalid - generate a new one from Google