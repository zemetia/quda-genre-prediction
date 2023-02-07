from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

def returnJSON(data) -> HttpResponse:
    json_object = json.dumps(data, indent = 4) 
    return HttpResponse(json_object, content_type="application/json")

def redirect(path: str) -> HttpResponse:
    return HttpResponseRedirect(path)