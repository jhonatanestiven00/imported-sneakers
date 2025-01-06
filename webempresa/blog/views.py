from django.shortcuts import render, get_object_or_404
from .models import PostDB, CategoryDB

# Create your views here.
def Blog(request):
    posts= PostDB.objects.all()
    return render(request,'blog/blog.html',{'posts':posts}) 

def category(request, category_id):
    category= get_object_or_404(CategoryDB,id=category_id)
    return render(request, "blog/category.html",{'category':category})