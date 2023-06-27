from django.urls import path 
from parserAPI import views

# define the urls
urlpatterns = [
    path('instantParse/', views.instantParse),
    #path('findParser/', views.findParse),
    path('submit/', views.addParse)
]