from django.shortcuts import render, get_object_or_404
from .models import PageDB

# Create your views here.

def page(request, page_id, page_slug):
    page= get_object_or_404(PageDB,id=page_id)
    return render(request,'pages/sample.html', {'page':page})
