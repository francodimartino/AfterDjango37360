from django.http import HttpResponse
from django.shortcuts import render

from .models import Persona
from django.template import  loader
# Create your views here.

def inicioApp(request):
    nom="Franco"
    ape="Di Martino"
    lista_de_notas=[9,5,3,8,7,1,9,3,8]

    diccionario={'nombre':nom,'apellido':ape, 'lista':lista_de_notas}

    template=loader.get_template('AppPersonas/inicio.html')
    
    documento=template.render(diccionario)
    return HttpResponse(documento)

def crearPersona(request):

    persona=Persona(nombre='Juan', apellido='Perez', edad=20)
    persona.save()
    texto= f"Se creo la persona {persona.nombre} {persona.apellido} con edad {persona.edad}"
    return HttpResponse(texto)

def nuevo(request):
    return render(request, "AppPersonas/nuevo.html")

