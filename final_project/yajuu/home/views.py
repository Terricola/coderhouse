from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

# def index(request):
    
#     mi_html = open(r"D:\User\Documents\Cursos\repositorios_git\coderhouse\final_project\yajuu\home\static\home\index.html")

#     plantilla = Template(mi_html.read())

#     mi_html.close()

#     mi_contexto = Context()

#     documento = plantilla.render(mi_contexto)

#     return HttpResponse(documento)


