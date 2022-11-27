from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=40)
    tag = models.CharField(max_length=25)
    description = RichTextField(null=True, blank=True)
    #image = models.ImageField(upload_to='post', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        unique_together = (
            "title",
            "tag",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Pregunta: {self.title} | Categoria: {self.tag} | Descripción: {self.description}"

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)