from django.shortcuts import render

from apps.models import People


# Create your views here.

def index_view(request):
    contex = {
        "peoples": People.objects.all()
    }
    return render(request, 'apps/index.html', contex)

