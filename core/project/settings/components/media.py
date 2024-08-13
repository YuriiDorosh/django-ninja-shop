import os.path

from core.project.settings.components.static import STATIC_DIR


MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(STATIC_DIR, "media/")
