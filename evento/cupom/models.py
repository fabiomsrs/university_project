from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

# Create your models here.

class Cupom(models.Model):
	nome_cupom = models.CharField(max_length=25)
	desconto = models.PositiveIntegerField(validators=[MaxValueValidator(100)])		
	data_de_inicio = models.DateTimeField(null=True)
	data_de_fim = models.DateTimeField(null=True)	

	def __str__(self):
		return self.nome_cupom,

class CupomAutomatico(Cupom):
	evento = models.OneToOneField('evento.Evento',related_name='meus_cupons',default='')

	def descontar_valor_evento(self):
		pass
