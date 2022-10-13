from django.db import models

# Create your models here.
class BasicData(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return f"Name: {self.name} | Last Name: {self.last_name} | Age: {self.age} | Birth date: {self.birth_date}"
