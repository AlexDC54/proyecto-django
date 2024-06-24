from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,'contenido/principal.html')
def curso(request):
    return render(request,'contenido/curso.html')
def contacto(request):
    return render(request,'contenido/contacto.html')

def mi_pagina(request):
    return render(request, 'contenido/base.html')

