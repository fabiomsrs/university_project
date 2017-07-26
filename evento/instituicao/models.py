from django.db import models

# Create your models here.

class Instituicao(models.Model):
	nomeInstituicao = models.CharField(max_length=25)
	uf = models.CharField(max_length=2)
	#TODO listas de tags

