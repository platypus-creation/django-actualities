from django.contrib import admin
from actualities.models import Actuality
from django.conf import settings
    
class ActualityAdmin(admin.ModelAdmin):
    class Media:
      js = [settings.ADMIN_MEDIA_PREFIX+'tinymce/jscripts/tiny_mce/tiny_mce.js', settings.STATIC_URL+'admin/js/tinymce_setup.js',]
    
    
admin.site.register(Actuality, ActualityAdmin)

