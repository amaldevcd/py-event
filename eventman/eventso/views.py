from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"eventso/index.html")

@login_required
def theme(request):
    return render(request,"eventso/theme.html")

def signuptheme(request):
    return render(request,"eventso/signuptheme.html")