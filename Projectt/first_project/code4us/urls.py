from django.urls import path
from code4us import views

urlpatterns= [
     path("",views.home),
     path("home",views.home),
     path("books",views.books), 
]
        