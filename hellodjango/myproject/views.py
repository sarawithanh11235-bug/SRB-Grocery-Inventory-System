from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. DJANGO SERVER
# Email: sblet0001@mail.ct.edu
# Username: sarah
# PW: *************
# http://127.0.0.1:8000/

def hello(request):
    return HttpResponse('<h1>Grocery Inventory System with Django!</h1>')


