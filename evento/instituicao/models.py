from django.db import models

# Create your models here.

class Instituicao(models.Model):
	nome_instituicao = models.CharField(max_length=25)
	uf = models.CharField(max_length=2)

