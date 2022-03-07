import mouth_detection
import correction_module_code
import feedbackmodule
import mixmodule
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def initial_view(request):
    return render(request, "initial.html")

def home_view(request):
    context= {}
    context['user']= request.user
    return render(request, "home.html",context)

def feedback_module_view(request):
    # context= {}
    # context['user']= request.user
    a2 = feedbackmodule.feedback_code()
    return render(request, "home.html")

def mix_module_view(request):
    # context= {}
    # context['user']= request.user
    a3 = mixmodule.mixmodulecode()
    context= {}
    context['prediction']= a3
    return render(request, "final_output.html", context)

def mouth_detect_view(request):
    a1 = mouth_detection.detect_mouth()
    return render(request, "home.html")

def correction_module_view(request):
    context= {}
    context['user']= request.user
    return render(request, "correction_module.html", context)

@csrf_exempt
def correction_module_view_use(request):
    
    text = request.body.decode('utf8').replace("'", '"').replace("+", " ").replace("data=", "")
    final_value = correction_module_code.run_this(text)
    print(final_value)
    return StreamingHttpResponse(final_value)
