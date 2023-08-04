from django.contrib import admin
from . import views
from django.http import HttpResponse
# from django.conf.urls import url
from django.urls import include, path
urlpatterns = [
    # Notice the URL has been named
    path('object_detection/', views.objectDetection, name='object_detection'),
]