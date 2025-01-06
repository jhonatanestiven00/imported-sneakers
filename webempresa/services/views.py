from django.shortcuts import render
from . import models
# Create your views here.

def Services(request):
    projects= models.ServiceDB.objects.all()
    return render(request,'services/services.html',{'projects': projects}) 