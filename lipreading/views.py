import mouth_detection
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.shortcuts import render
  
# Create your views here.
def home_view(request):
    return render(request, "home.html")

def mouth_detect_view(request):
    a1 = mouth_detection.detect_mouth()
    return render(request, "home.html")
