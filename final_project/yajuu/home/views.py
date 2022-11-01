from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

from post.models import Post

# Create your views here.
def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(title__contains=search_param)
        query.add(Q(description__contains=search_param), Q.OR)
        posts = Post.objects.filter(query)
        context_dict.update(
            {
                "posts": posts,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )


# En costruccion:
# def contact(request):
#         return render(
#         request=request,
#         context={},
#         template_name="home/contact.html",
#     )


# def index(request):
    
#     mi_html = open(r"D:\User\Documents\Cursos\repositorios_git\coderhouse\final_project\yajuu\home\static\home\index.html")

#     plantilla = Template(mi_html.read())

#     mi_html.close()

#     mi_contexto = Context()

#     documento = plantilla.render(mi_contexto)

#     return HttpResponse(documento)


