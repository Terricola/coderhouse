from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=25)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=15)

    def __str__(self):
        return f"Nombre: {self.name} | Correo: {self.email} | Usuario: {self.username} | Contraseña: {self.password}"
