from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Inscricao(models.Model):	
	usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='minhas_inscricoes')	
	evento = models.ForeignKey('core.Evento', on_delete=models.CASCADE, related_name='minhas_inscricoes')
	atividades = models.ManyToManyField('core.Atividade')
	cupom = models.OneToOneField('Cupom',related_name='minha_inscricao',null=True)
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
	evento = models.OneToOneField('core.Evento',related_name='meus_cupons',default='')

	def descontar_valor_evento(self):
		if self.evento in EventoInscrevivel.objects.all():
			e = EventoInscrevivel.objects.get(pk = self.evento.pk)
			e.valor = e.valor * (1 - self.desconto/100)
			e.save()			
			return e.valor
		else:
			for atividade in Atividade.objects.filter(evento=self.evento):
				atividade.valor = atividade.valor * (1 - self.desconto/100)
				atividade.save()
			return [atividade.valor for atividade in Atividade.objects.filter(evento=self.evento)]				

class Pagamento(models.Model):	
	valor_total = models.FloatField(null=True)
	pago = models.BooleanField(default=False)	
	inscricao = models.OneToOneField('inscricao.Inscricao',related_name='meu_pagamento',default='')

	def is_pago(self):
		return self.pago
			
	#Calcular_Valor_Total atribui ao valor total, o valor de todas atividades que inscricao possui
	def calcular_valor_total(self):
		itens = self.inscricao.atividades.all()
		self.valor_total = 0
		for i in itens:
			self.valor_total += i.valor

		return self.valor_total

	def save(self, *args, **kwargs):		
		self.calcular_valor_total()
		super(Pagamento, self).save(*args, **kwargs)

from core.models import Evento,EventoInscrevivel,Atividade