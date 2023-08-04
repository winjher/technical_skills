from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView  # Import TemplateView
import os
import pickle
from django.utils.deconstruct import deconstructible
@deconstructible

# Create your views here.
def Segment(request):
    # Get all Posts
    return render(request, 'template/segment.html')