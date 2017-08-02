from django.db import models

from inscricao.models import RelacionamentoAtividadeInscricao
# Create your models here.

class Pagamento(models.Model):	
	valor_total = models.FloatField(null=True)
	pago = models.BooleanField(default=False)	
	inscricao = models.OneToOneField('inscricao.Inscricao',related_name='meu_pagamento',default='')

	def is_pago(self):
		return self.pago

	def get_incricao(self):
		return self.inscricao.get()

	def get_valor_total(self):
		return self.valor_total
		
	#setValorTotal atribui ao valor total, o valor de todas atividades que inscricao possui
	def set_valor_total(self):
		relacionamentos = RelacionamentoAtividadeInscricao.objects.filter(inscricao = self.inscricao)
		self.valor_total = 0
		for i in relacionamentos:
			self.valor_total += i.atividade.valor_atividade
		self.save()	