from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request,'core/index.html') 
def About(request):
    return render(request,'core/about.html') 

def Store(request):
    return render(request,'core/store.html') 



