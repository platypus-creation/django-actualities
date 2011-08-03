from django.shortcuts import render, get_object_or_404
from actualities.models import Actuality

def list(request):
    last_actualities = Actuality.objects.published()
    return render(request, 'actualities/list.html', locals())
    
def actuality(request, year, month, day, slug):
    actuality = get_object_or_404(Actuality.objects.published(), slug=slug)
    return render(request, 'actualities/actuality.html', locals())