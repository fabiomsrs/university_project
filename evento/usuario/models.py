from django.db import models

# Create your models here.
class Usuario(models.Model):
	nomeUsuario = models.CharField(max_length=25)
	login = models.CharField(max_length=25)
	password = models.CharField(max_length=25)

class Inscricao(models.Model):	
	usuario = models.ForeignKey('Usuario')	
	evento = models.ForeignKey('evento.Evento',default='')
	atividade = models.ManyToManyField('evento.Atividade', through='RelacionamentoAtividadeInscricao')
		
class RelacionamentoAtividadeInscricao(models.Model):
	atividade = models.ForeignKey('evento.Atividade',default='')
	inscricao = models.ForeignKey('Inscricao',default='')