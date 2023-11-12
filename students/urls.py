
from django.urls import path
from . import views


app_name = "students"
urlpatterns = [

    path('',views.about, name= "about"),
    path('contact/', views.contact, name="contact"),
    path('classes/', views.classes, name="classes"),

]
