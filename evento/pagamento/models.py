from django.db import models

from inscricao.models import RelacionamentoAtividadeInscricao
# Create your models here.

class Pagamento(models.Model):	
	valorTotal = models.FloatField(null=True)
	pago = models.BooleanField(default=False)	
	inscricao = models.OneToOneField('inscricao.Inscricao',related_name='meu_pagamento',default='')
	def getValorTotal(self):
		relacionamentos = RelacionamentoAtividadeInscricao.objects.filter(inscricao = self.inscricao)
		valorTotal = 0
		for i in relacionamentos:
			valorTotal += i.atividade.valorAtividade

		return valorTotal