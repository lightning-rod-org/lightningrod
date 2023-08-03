from django.urls import path 
from parserAPI import views

app_name = 'parserAPI'

# define the urls
urlpatterns = [
    path('status/', views.instantParse, name='status'),
    path('submit/', views.addParse, name='addParse'),
    path('parsers/', views.getParsers, name='getParsers')
]
