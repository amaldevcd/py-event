from django.urls import include,path
from django.urls import path
from . import views


urlpatterns =[
    path('', views.index ,name="index"),
    path('home/', views.home , name="home"),
    path('signup/',views.signuptheme , name="signup"),
    path('host/',views.host,name="host"),
]