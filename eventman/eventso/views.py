from eventso.models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"eventso/index.html")

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request,"eventso/home.html",{'posts':posts})

def signuptheme(request):
    return render(request,"eventso/signuptheme.html")