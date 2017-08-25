from django.db import models
from django.core.validators import MaxValueValidator
from .managers import CupomAutomaticoManager
from django.utils import timezone

# Create your models here.

class Cupom(models.Model):
	nome_cupom = models.CharField(max_length=25)
	desconto = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
	evento = models.ForeignKey('evento.Evento',related_name='meus_cupons',default='')
	isautomatico = models.BooleanField()
	data_de_inicio = models.DateTimeField(null=True)
	data_de_fim = models.DateTimeField(null=True)
	objects = CupomAutomaticoManager()

	def __str__(self):
		return self.nome_cupom,