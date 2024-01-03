from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
#     return HttpResponse("Hello world!!!")

class Index(TemplateView):
    template_name = 'home/index.html'