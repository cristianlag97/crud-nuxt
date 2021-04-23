from django.db import models

class Autor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    anno_nacimiento = models.DateField()
    anno_fallece    = models.DateField(null=True, blank=True)

class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    compras = models.IntegerField()