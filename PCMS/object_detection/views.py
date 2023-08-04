from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView  # Import TemplateView
import os
import pickle
from django.utils.deconstruct import deconstructible
@deconstructible


# create your views here and add parameters title
def objectDetection(request):
    
    # Get all Posts
    return render(request, 'template/objectDetection.html')

