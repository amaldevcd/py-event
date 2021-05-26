from django.contrib.auth.models import User
from django.http import response
from eventso.models import Post
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request,"eventso/index.html")

@login_required
def home(request):
    posts = Post.objects.order_by("event_date")
    return render(request,"eventso/home.html",{'posts':posts})

@login_required
def host(request):
    form=PostForm(request.POST or None)
    name =request.user
    if form.is_valid():
        form.save()
    context = { 'form':form} 
    return render(request,"eventso/host.html",context)
    
     
        
        


def signuptheme(request):
    return render(request,"eventso/signuptheme.html")




