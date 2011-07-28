from django.conf import settings

ACTUALITIES_UPLOAD = 'uploads/'
if hasattr(settings, 'ACTUALITIES_UPLOAD'):
    ACTUALITIES_UPLOAD = settings.ACTUALITIES_UPLOAD