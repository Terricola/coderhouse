from post.models import Post
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import PostForm

# Create your views here.
# Permite agregar datos al modelo User a traves de un formulario
def post_form(request):

    if request.method == "POST":

        my_form = PostForm(request.POST)
        
        print(my_form)

        if my_form.is_valid:

            information = my_form.cleaned_data

            data = Post(
                title = information["title"],
                tag = information["tag"],
                description = information["description"]
            )

            data.save()

            return render(
                request=request,
                template_name="post_index.html",
            )          
    
    else:
        my_form = PostForm()
    return render(request, "post_index.html", {"my_form":my_form})

# Ver lista de preguntas actuales en la base de datos
def post_detail(request):
    event_list = Post.objects.all()
    template = loader.get_template("post_detail.html")
    context_dict = {"event_list": event_list}
    render = template.render(context_dict)
    return HttpResponse(render)

def create_model_view(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post/post_index.html"