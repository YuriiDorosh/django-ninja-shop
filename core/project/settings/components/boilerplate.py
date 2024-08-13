from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


ROOT_URLCONF = 'core.project.urls'

WSGI_APPLICATION = 'core.project.wsgi.application'
