from django.shortcuts import render
from django.http import HttpResponse



def homepage(request):
    return HttpResponse("<h1>Hi, django Framework is Easy to learn.</h1>")
