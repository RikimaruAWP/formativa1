from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Notes, Listado

l = Listado()

def home(request):
    return render(request, 'cores/home.html')

def note(request):
    return render(request, 'cores/notas.html', {'notes': l.list})

def create_notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_important = request.POST.get('is_important') == 'on'

        if not title or not description:
            mensaje = 'Todos los campos son obligatorios'
        else:
            n = Notes(title=title, description=description, is_important=is_important)
            mensaje = l.agregar(n)
        return render(request, 'cores/create.html', {'mensaje': mensaje})
    else:
        return render(request, 'cores/notas.html')

def eliminar(request, title):
    print(title)
    return render(request, 'cores/confirm_delete.html', {'title': title})

def delete_notes(request):
    title = request.POST.get('title')
    if title == '':
        mensaje = 'Se ha producido un error'
    else:  
        mensaje = l.eliminar(title)
    return render (request, 'cores/delete.html', {'mensaje':mensaje})