from mod.models import Moderator
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import ModForm


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
            messages.success(
                request,
                f"El usuario {information['name']} ha sido creado exitosamente"
            )

            return render(
                request=request,
                template_name="mod_form.html",
            )          
    
    else:
        my_form = ModForm()
    return render(request, "mod_form.html", {"my_form":my_form})