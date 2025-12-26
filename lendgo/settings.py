# lendgo/settings.py

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Build paths inside the project like this: BASE_DIR / 'subdir'.
SETTINGS_DIR = Path(__file__).resolve().parent

# --- 1. Core Settings ---
# WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key-goes-here'  # Replace with a secure key in production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# --- 2. Application Definition ---

INSTALLED_APPS = [
    # Default Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
    'users.apps.UsersConfig',
    'tools.apps.ToolsConfig',
    'borrowing.apps.BorrowingConfig',
    'reviews.apps.ReviewsConfig',

    # Third-party Apps (If any, e.g., Crispy Forms, Debug Toolbar)
    # 'crispy_forms',
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

ROOT_URLCONF = 'lendgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Look for project-level templates here
        # This line must use the variable that points to the correct place (BASE_DIR)
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lendgo.wsgi.application'

# --- 3. Database ---
# Using SQLite3 as the default database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Set the name to be next to manage.py/settings.py
        'NAME': SETTINGS_DIR / 'db.sqlite3',
    }
}

# --- 4. Password Validation ---

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

# --- 5. Internationalization ---

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# --- 6. Static and Media Files (For CSS, JS, Images) ---

# URL prefix for static files.
STATIC_URL = '/static/'

# List of directories where Django should additionally look for static files
# (i.e., your project-wide static files, like a vendor JS library or global CSS).
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# The directory where static files will be collected for deployment (when running collectstatic).
# STATIC_ROOT = BASE_DIR / 'staticfiles' # Uncomment for production

# URL prefix for media files (user uploads).


# Absolute filesystem path to the directory that will hold user-uploaded files.
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# --- 7. Custom User Model and Auth Settings ---

# Use your custom user model for authentication
AUTH_USER_MODEL = 'users.CustomUser'

# Redirect URLs
LOGIN_REDIRECT_URL = 'home'  # <-- Use 'home' (or 'tools') instead of 'dashboard'  # Assuming you have a 'dashboard' URL name
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'  # The name of the URL pattern for the login page

# --- 8. Default Primary Key Field Type ---

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'