from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"eventso/index.html")

def theme(request):
    return render(request,"eventso/theme.html")