from mod.models import Moderator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import ModForm

# Para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def mod_form(request):

    if request.method == "POST":

        my_form = ModForm(request.POST)
        
        print(my_form)

        if my_form.is_valid:

            information = my_form.cleaned_data

            data = Moderator(
                name = information["name"],
                email = information["email"],
                age = information["age"],
                username = information["username"],
                password = information["password"]
            )

            data.save()
            #messages.success(request, f"El usuario {information['username']} ha sido creado exitosamente")
            messages.success(request, f"Gracias por enviar tu solicitud {information['name']}")

            return render(
                request=request,
                template_name="home/index.html",
            )          
    
    else:
        my_form = ModForm()
    return render(request, "mod_form.html", {"my_form":my_form})

# Revisar si son necesarias las dos funciones abajo o si solo con
# modificar la de arriba es suficiente

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, "mod_form.html", {"mensaje":f"Bienvenido {username}"})
            else:
                return render(request, "mod_form.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "mod_form.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
    

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = ModForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"mod_form.html",  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = ModForm()     

      return render(request,"register.html" ,  {"form":form})