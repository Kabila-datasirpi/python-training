from django.shortcuts import render
from django.http import HttpResponse

def display_text(request):
    return HttpResponse("Hello, this is a simple text message!")



