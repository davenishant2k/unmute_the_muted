import mouth_detection
import correction_module_code
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.shortcuts import render
  
# Create your views here.
def home_view(request):
    return render(request, "home.html")

def mouth_detect_view(request):
    a1 = mouth_detection.detect_mouth()
    return render(request, "home.html")

def correction_module_view(request):
    return render(request, "correction_module.html")

def correction_module_view_use(request):
    
    final_value = correction_module_code.run_this('there are too apples')
    print(final_value)
    context = {}
    context["final_value"] =final_value
    return render(request, "correction_module.html", context)
