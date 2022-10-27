from users.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
# Formulario para agregar datos al modelo User
def user_form(request):
    return render(request, "user_form.html")


# Permite ver los datos actuales en la base de datos
def show_data(request):

    event_list = User.objects.all()
    template = loader.get_template("index_family.html")
    context_dict = {"event_list": event_list}
    render = template.render(context_dict)
    return HttpResponse(render)