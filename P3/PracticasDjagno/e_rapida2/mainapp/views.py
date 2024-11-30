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

def redireccion_inicio(request, exception):
    return render(request, 'mainapp/404.html')

def redireccion_inicio(request, exception):
    return render(request, 'mainapp/404.html')


def registrarse(request):
    return render(request,'user/registrarse.html',{
        'title':'registro',
        'content':'..:: !hola!  registro ::..'
    })

def inicio_sesion(request):
    return render(request,'user/login.html',{
        'title':'inicio de sesion',
        'content':'..:: !hola!  soy login ::..'
        
    })
