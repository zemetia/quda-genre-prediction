from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse
from transformers import TFAutoModel, TFBertTokenizer, TFBertModel
import numpy as np
import pandas as pd
import tensorflow as keras
from . import controller

def get_genres(data, total, genre_summary, tolerance=0.3):
    result = []
    for i in range(total):
        if data[i] > tolerance: result.append(genre_summary[i])
    return result

def predict(sinopsys: str) -> list:
    # gass prediksi cok
    # result = fullmodel.predict([input])
    # result = []
    # return get_genres(result[0])
    return ["adawdawd"]

def index(request) -> HttpResponse:
    if request.method == "POST":
        sinopsys = request.POST['sinopsys']
        result = predict(sinopsys)
        
        return controller.returnJSON({
            "sinopsys": sinopsys,
            "genres": result
            })
    
    elif request.method == "GET": 
        return controller.redirect('/')