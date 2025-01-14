from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=15)
    description = models.TextField()
    
    def __str__(self):
        return self.name
         
    class Meta:
            verbose_name = "Categoria"
            verbose_name_plural = "Categorias"

class Professor(User):
    numero_trabajador = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"


class Student(User):
    matricula = models.CharField(max_length=12)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
