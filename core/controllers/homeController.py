from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from . import controller

def index(request):
    if request.method == "GET":
        result = ["Hentai", "Ecchi", "Action"]
        return render(request, 'home/index.html', {"genres": result})
    