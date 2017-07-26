from django.db import models

# Create your models here.
class Usuario(models.Model):
	nome_usuario = models.CharField(max_length=25)
	login = models.CharField(max_length=25)
	password = models.CharField(max_length=25)

