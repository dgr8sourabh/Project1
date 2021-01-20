from django.shortcuts import render
from django.http import HttpResponse



def homepage(request):
    return HttpResponse("<center><h1>Welcome to django Framework.</h1></center>")
