from django import forms

class UserForm(forms.Form):

    name = forms.CharField(
        max_length=40,
        label="Nombre",
        required=False,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 1.3em',
                "class": "name",
                "placeholder": "nombre completo",
                "required": True,
            }
        ),
    )

    email = forms.EmailField(
        max_length=25,        
        label="Correo",
        required=False,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 1.3em',
                "class": "email",
                "placeholder": "correo",
                "required": True,
            }
        ),
    )

    username = forms.CharField(
        max_length=12,
        label="Usuario",
        required=False,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 1.3em',
                "class": "username",
                "placeholder": "12 caracteres max.",
                "required": True,
            }
        ),
    )
    
    password = forms.CharField(
        max_length=15,
        label="Contraseña",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'style': 'font-size: 1.3em',
                "class": "password",
                "placeholder": "15 caracteres max.",
                "required": True,
            }
        ),
    )
