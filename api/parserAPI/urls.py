from django.urls import path 
from parserAPI import views

app_name = 'parserAPI'

# define the urls
urlpatterns = [
    path('instantParse/', views.instantParse, name='instantParse'),
    #path('findParser/', views.findParse),
    path('submit/', views.addParse, name='addParse')
]