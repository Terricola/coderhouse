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
                'style': 'font-size: 1.3em',
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
                'style': 'font-size: 1.3em',
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
                'style': 'font-size: 1.3em',
                "class": "description",
                "placeholder": "Por favor agrega una despcripción a tu pregunta",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Post
        fields = ["title", "tag", "description"]

class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingresar comentario",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )