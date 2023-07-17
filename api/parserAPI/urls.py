from django.urls import path 
from parserAPI import views
from parserAPI.views import addParse
# define the urls
urlpatterns = [
    path('instantParse/', views.instantParse),
    #path('findParser/', views.findParse),
    path('submit/', addParse),
    path('asynctest/', views.asynctest),
    path('test/', views.index),

]