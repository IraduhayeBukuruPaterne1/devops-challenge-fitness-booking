import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-your-secret-key')  # Secure secret key
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'fitness_booking_db'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# Add this setting to collect static files into the staticfiles directory
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
