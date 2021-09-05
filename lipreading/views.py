import mouth_detection
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.shortcuts import render
  
# Create your views here.
def home_view(request):
    return render(request, "home.html")

def mouth_detect_view(request):
    mouth_detection.detect_mouth()
    return None
