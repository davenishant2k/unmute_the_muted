import mouth_detection
import correction_module_code
import feedbackmodule
import mixmodule
from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def logout_view(request):
    logout(request)

def initial_view(request):
    context= {}
    context['message'] = ""
    return render(request, "initial.html")

def home_view(request):
    if request.user.is_authenticated:
        context= {}
        context['user']= request.user
        return render(request, "home.html",context)
    else:
        context = {}
        context['message'] = "Please login before accessing the Application"
        return render(request, "initial.html", context)

def contact_us_view(request):
    if request.user.is_authenticated:
        context= {}
        context['user']= request.user
        return render(request, "contact_us.html",context)
    else:
        context = {}
        context['message'] = "Please login before accessing the Application"
        return render(request, "initial.html", context)

def about_us_view(request):
    if request.user.is_authenticated:
        context= {}
        context['user']= request.user
        return render(request, "about_us.html",context)
    else:
        context = {}
        context['message'] = "Please login before accessing the Application"
        return render(request, "initial.html", context)

def feedback_module_view(request,corrected_text):
    # context= {}
    # context['user']= request.user
    a2 = feedbackmodule.feedback_code(request.user, corrected_text)
    return render(request, "home.html")

def mix_module_view(request,speaker):
    if request.user.is_authenticated:
        corrected_list = mixmodule.mixmodulecode(speaker)
        context= {}
        context['output']= corrected_list[0]
        return render(request, "new_final_output.html", context)
    else:
        context = {}
        context['message'] = "Please login before accessing the Application"
        return render(request, "initial.html", context)
    

def mouth_detect_view(request):
    if request.user.is_authenticated:
        a1 = mouth_detection.detect_mouth()
        return render(request, "home.html")
    else:
        context = {}
        context['message'] = "Please login before accessing the Application"
        return render(request, "initial.html", context)

def correction_module_view(request):
    context= {}
    context['user']= request.user
    return render(request, "correction_module.html", context)

def new_final_output_view(request):
    context = {}
    context['output'] = ""
    return render(request, "new_final_output.html", context)

@csrf_exempt
def correction_module_view_use(request):
    
    text = request.body.decode('utf8').replace("'", '"').replace("+", " ").replace("data=", "")
    final_value = correction_module_code.run_this(text)
    print(final_value)
    return StreamingHttpResponse(final_value)
