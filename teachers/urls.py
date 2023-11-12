
from django.urls import path
from . import views


app_name = "teachers"
urlpatterns = [
    path('teachers/',views.home, name= "home")

]
