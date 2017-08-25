from django.db import models

class Pagamento(models.Model):	
	valor_total = models.FloatField(null=True)
	pago = models.BooleanField(default=False)	
	inscricao = models.OneToOneField('inscricao.Inscricao',related_name='meu_pagamento',default='')

	def is_pago(self):
		return self.pago
			
	#Calcular_Valor_Total atribui ao valor total, o valor de todas atividades que inscricao possui
	def calcular_valor_total(self):
		relacionamentos = self.inscricao.relacionamentoatividadeinscricao_set.all()
		self.valor_total = 0
		for i in relacionamentos:
			self.valor_total += i.atividade.valor_atividade

		return self.valor_total

	def save(self, *args, **kwargs):		
		self.calcular_valor_total()
		super(Pagamento, self).save(*args, **kwargs)

		