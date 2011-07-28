from django.contrib import admin
from actualities.models import Actuality, Version

class VersionAdmin(admin.StackedInline):
    model = Version
    extra = 0
    
class ActualityAdmin(admin.ModelAdmin):
    inlines = (VersionAdmin,)
    
admin.site.register(Actuality, ActualityAdmin)

