from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexView, name='home'),
    path('about/',views.About, name='about'),
    path('store/',views.Store, name='store'),
]