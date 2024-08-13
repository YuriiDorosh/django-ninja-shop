import os
import sys

from core.project.settings.components.boilerplate import BASE_DIR


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY = [
    "cachalot",
]

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


LOCAL_APPS = [
    'core.apps.products.apps.ProductsConfig',
    'core.apps.customers.apps.CustomersConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS
