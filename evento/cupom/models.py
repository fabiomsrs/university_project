from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
from evento.models import Evento,EventoInscrevivel,Atividade

# Create your models here.

class Cupom(models.Model):
	nome_cupom = models.CharField(max_length=25)
	desconto = models.PositiveIntegerField(validators=[MaxValueValidator(100)])		
	data_de_inicio = models.DateTimeField(null=True)
	data_de_fim = models.DateTimeField(null=True)	

	def usar_desconto(self):
		if self.minha_inscricao != None:
			self.minha_inscricao.meu_pagamento = self.minha_inscricao.meu_pagamento * (1 - self.desconto/100)			

	def __str__(self):
		return self.nome_cupom,

class CupomAutomatico(Cupom):
	evento = models.OneToOneField('evento.Evento',related_name='meus_cupons',default='')

	def descontar_valor_evento(self):
		if self.evento in EventoInscrevivel.objects.all():
			e = EventoInscrevivel.objects.get(pk = self.evento.pk)
			e.valor = e.valor * (1 - self.desconto/100)
			e.save()			
		else:
			for atividade in Atividade.objects.filter(evento=self.evento):
				atividade.valor = atividade.valor * (1 - self.desconto/100)
				atividade.save()
