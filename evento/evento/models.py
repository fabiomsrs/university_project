from django.db import models

# Create your models here.

class Atividade(models.Model):
	nome_atividade = models.CharField(max_length=25)	
	descricao = models.CharField(max_length=25)
	valor_atividade = models.FloatField(null=True)	
	evento = models.ForeignKey('Evento',related_name='minhas_atividades',default='')
		
class Evento(models.Model):
	nome_evento = models.CharField(max_length=25)
	instituicao = models.ManyToManyField('instituicao.Instituicao')
	usuario_criador = models.ForeignKey('auth.User',related_name='meus_eventos',default='')	
	
	def inscricoes_pagas(self):
		inscricoes = self.minhas_inscricoes.get_queryset()
		return inscricoes.filter(meu_pagamento__pago=True)

class Cupom(models.Model):
	desconto = models.IntegerField()
	evento = models.ForeignKey('Evento',related_name='meus_cupons',default='')	
	
