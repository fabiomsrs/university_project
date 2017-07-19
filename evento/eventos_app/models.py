from django.db import models

class Usuario(models.Model):
	nome = models.charField(max_length=25)
	login = models.charField(max_length=25)
	password = models.charField(max_length=25)

class Evento(models.Model):
	usuario = models.ForeignKey('Usuario')	

class Atividade(models.Model):
	nome = models.charField(max_length=25)	
	descricao = models.charField(max_length=25)
	atividade = models.ForeignKey('Evento')

class Inscricao(models.Model):
	valor = models.IntegerField()

class Cupom(models.Model):
	desconto	 = models.IntegerField()
	inscricao = models.ForeignKey('Inscricao')
