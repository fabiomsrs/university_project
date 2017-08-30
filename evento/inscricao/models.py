from django.db import models
from evento.models import Evento
# Create your models here.

class Inscricao(models.Model):	
	usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='minhas_inscricoes')	
	evento = models.ForeignKey('evento.Evento', on_delete=models.CASCADE, related_name='minhas_inscricoes')
	cupom = models.OneToOneField('cupom.Cupom',related_name='meu_cupom',null=True)
	#inscricao = models.OneToOneField('inscricao.Inscricao',related_name='meu_pagamento',default='')	
	#atividade = models.ManyToManyField('evento.Atividade', through='RelacionamentoAtividadeInscricao')

	def __str__(self):
		return self.usuario.first_name

	def save(self, *args, **kwargs):
		#evitar inscricoes repetidas
		for inscricao in Inscricao.objects.all():
			if self.evento == inscricao.evento and self.usuario == inscricao.usuario:
				raise Exception('Inscricao ja existe')			
		super(Inscricao, self).save(*args, **kwargs)

class ItemInscricao(models.Model):
	inscricao = models.ForeignKey('Inscricao', on_delete=models.CASCADE, related_name='meus_itens')
	atividade = models.ForeignKey('evento.Atividade')