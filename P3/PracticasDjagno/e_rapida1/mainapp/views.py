from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'mainapp/index.html',{
        'title':'Inicio Pagina Principal',
        'content':'..:: !Bienvenido a mi pagina principal! ::..'
    })

def about(request):
    return render(request,'mainapp/about.html',{
        'title':'sobre mi',
        'content':'..:: !hola! soy about ::..'
    })

def mision(request):
    return render(request,'mainapp/mision.html',{
        'title':'mision',
        'content':'..:: !hola! soy mision ::..'
    })

def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'vision',
        'content':'..:: !hola!  soy vision ::..'
    })