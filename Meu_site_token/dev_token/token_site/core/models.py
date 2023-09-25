from django.db import models

# Create your models here.
class Registro(models.Model):
    nome = models.CharField(max_length=50, default=None)
    email = models.EmailField()

    is_verfied = models.BooleanField(default=False)
    token = models.CharField(max_length = 100, default=None)