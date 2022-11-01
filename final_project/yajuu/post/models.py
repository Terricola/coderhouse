from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=40)
    tag = models.CharField(max_length=25)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"Pregunta: {self.title} | Categoria: {self.tag} | Descripción: {self.description}"