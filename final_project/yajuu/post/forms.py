from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Post

tag_choices = [
    ("vida cotidiana", "Vida cotidiana"),
    ("tecnologia", "Tecnologia"),
    ("cocina", "Cocina"),
    ("debate", "Debate"),
]

class PostForm(forms.ModelForm):

    title = forms.CharField(
        max_length=40,
        label="Titulo de pregunta",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "title",
                "placeholder": "Pregunta",
                "required": True,
            }
        ),
    )

    tag = forms.CharField(
        max_length=25,        
        label="Tema",
        required=False,
        widget=forms.Select(
            choices=tag_choices,
            attrs={
                "class": "tag",
                "placeholder": "Categoria tema",
                "required": True,
            }
        ),
    )

    description = forms.CharField(
        #max_length=12,
        label="Descripción",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "description",
                "placeholder": "Por favor agrega una despcripción a tu pregunta",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Post
        fields = ["title", "tag", "description"]