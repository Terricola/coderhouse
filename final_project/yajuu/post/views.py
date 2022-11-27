from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse
from django.template import loader


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from post.models import Post
from post.models import Comment
from .forms import PostForm
from .forms import CommentForm

# Create your views here.
# Ver lista de preguntas actuales en la base de datos con informacion limitada
class PostListView(ListView):
    model = Post
    paginate_by = 3

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
            messages.success(request, "Pregunta enviada exitosamente")

            return render(
                request=request,                
                template_name="home/index.html",
            )          
    
    else:
        my_form = PostForm()
    return render(request, "post_index.html", {"my_form":my_form})


# Ver todo el detalle de la pregunta seleccionada
class PostDetailView(DetailView):
    model = Post
    template_name ="post_detail.html"
    fields = ["title", "tag", "description"]

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        comments = Post.description
        comment_form = CommentForm()
        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post:post-list")

    form_class = PostForm
    # fields = ["name", "code", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate courses"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Post.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El curso {data['name']} - {data['code']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Curso {data['name']} - {data['code']} creado exitosamente!",
            )
            return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "tag", "description"]

    def get_success_url(self):
        course_id = self.kwargs["pk"]
        return reverse_lazy("post:post-detail", kwargs={"pk": course_id})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post:post-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        course = get_object_or_404(Post, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, course=course
        )
        comment.save()
        return redirect(reverse("course:course-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        course = self.object.course
        return reverse("course:course-detail", kwargs={"pk": course.id})


# def post_list(request):
#     event_list = Post.objects.all()
#     template = loader.get_template("post_list.html")
#     context_dict = {"event_list": event_list}
#     render = template.render(context_dict)
#     return HttpResponse(render)