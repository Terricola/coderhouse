import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.template import Template, Context

from home.forms import UserRegisterForm
from home.forms import UserUpdateForm
from home.forms import AvatarForm
from home.models import Avatar
from post.models import Post

# Create your views here.
def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"avatar_url": avatars[0].image.url}
    return {}

def index(request):
    return render(
        request=request,
        context=get_avatar_url_ctx(request),
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

def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("login")

    return render(
        request=request,
        context={"form": form},
        template_name="registration/register.html",
    )

@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home:index")

    form = UserUpdateForm(model_to_dict(user))
    return render(
        request=request,
        context={"form": form},
        template_name="registration/user_form.html",
    )

@login_required
def avatar_load(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid and len(request.FILES) != 0:
            image = request.FILES["image"]
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect("home:index")

    form = AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="home/avatar_form.html",
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


