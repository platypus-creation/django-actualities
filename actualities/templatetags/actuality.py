from django import template
from django.forms.widgets import CheckboxInput, RadioInput
from actualities.models import Actuality

register = template.Library()

@register.inclusion_tag('actualities/last_actualities.html')
def last_actualities(nb=4):
    last_actualities = Actuality.objects.published()
    return {
        'last_actualities': last_actualities[:nb]
    }

@register.inclusion_tag('actualities/last_actualities.html')
def filtered_actualities(tags, nb=4):
    if not hasattr(tags, '__iter__'):
        tags = [tags]
    last_actualities = Actuality.objects.published().filter(tags__name__in=tags).distinct()
    return {
        'last_actualities': last_actualities[:nb]
    }
    
