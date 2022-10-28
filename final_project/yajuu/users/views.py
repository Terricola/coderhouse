from users.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import UserForm

# Create your views here.
# Permite agregar datos al modelo User a traves de un formulario
def user_form(request):

    if request.method == "POST":

        my_form = UserForm(request.POST)
        
        print(my_form)

        if my_form.is_valid:

            information = my_form.cleaned_data

            data = User(
                name = information["name"],
                email = information["email"],
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
                template_name="user_form.html",
            )          
    
    else:
        my_form = UserForm()
    return render(request, "user_form.html", {"my_form":my_form})


# Permite ver los datos actuales en la base de datos
def show_data(request):

    event_list = User.objects.all()
    template = loader.get_template("index_family.html")
    context_dict = {"event_list": event_list}
    render = template.render(context_dict)
    return HttpResponse(render)