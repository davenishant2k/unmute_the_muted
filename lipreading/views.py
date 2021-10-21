import mouth_detection
import correction_module_code
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def home_view(request):
    return render(request, "home.html")

def mouth_detect_view(request):
    a1 = mouth_detection.detect_mouth()
    return render(request, "home.html")

def correction_module_view(request):
    return render(request, "correction_module.html")

@csrf_exempt
def correction_module_view_use(request):
    
    text = request.body.decode('utf8').replace("'", '"').replace("+", " ").replace("data=", "")
    final_value = correction_module_code.run_this(text)
    print(final_value)
    return StreamingHttpResponse(final_value)
