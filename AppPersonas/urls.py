from django.contrib import admin
from django.urls import include, path

from .views import inicioApp, crearPersona, nuevo

urlpatterns = [

      path('', inicioApp),    
      path('crearPersona/', crearPersona),  
      path('nuevo/', nuevo), 
    
]
