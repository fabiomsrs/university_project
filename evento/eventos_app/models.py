from django.db import models

class Usuario(models.Model):
	nomeUsuario = models.CharField(max_length=25)
	login = models.CharField(max_length=25)
	password = models.CharField(max_length=25)		

class Atividade(models.Model):
	nomeAtividade = models.CharField(max_length=25)	
	descricao = models.CharField(max_length=25)
	valorAtividade = models.FloatField()
	inscricao = models.ForeignKey('Inscricao')
	evento = models.ForeignKey('Evento')

class Inscricao(models.Model):	
	usuario = models.ForeignKey('Usuario')
	pagamento = models.ForeignKey('Pagamento')
	evento = models.ForeignKey('Evento')

class Pagamento(models.Model):
	valorTotal = models.FloatField()
	estadoPagamento = models.BooleanField(default=False)
	
class Cupom(models.Model):
	desconto = models.IntegerField()
	evento = models.ForeignKey('Evento')
	inscricao = models.ForeignKey('Inscricao')
	
class Evento(models.Model):
	nomeEvento = models.CharField(max_length=25)
	instituicao = models.ManyToManyField('Instituicao', through='Relacionamento')

class Instituicao(models.Model):
	nomeInstituicao = models.CharField(max_length=25)
	uf = models.CharField(max_length=2)
	#TODO listas de tags

class Relacionamento(models.Model):
	evento = models.ForeignKey('Evento')
	instituicao = models.ForeignKey('Instituicao')
	descricaoRelacionamento = models.CharField(max_length=25)




	
