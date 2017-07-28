from django.db import models

# Create your models here.
class Tag(models.Model):
	nome_tag = models.CharField(max_length=25)
	class Meta:
		abstract = True

class TagUsuario(Tag):	
	usuario = models.ManyToManyField('auth.User')

class TagEvento(Tag):
	evento = models.ManyToManyField('evento.Evento')