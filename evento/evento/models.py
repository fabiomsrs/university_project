from django.db import models

from enumfields import EnumField
from enumfields import Enum
# Create your models here.

class TipoEvento(Enum):
	EM_ANDAMENTO = 'em andamento'
	NOVO = 'novo'
	INSCRICOES_ABERTAS = 'inscricoes abertas'

class TipoAtividade(Enum):
	SEMINARIO = 'seminario'
	PALESTRA = 'palestra'
	SIMPOSIO = 'simposio'	
	DEFAULT = ''

class Atividade(models.Model):
	nome_atividade = models.CharField(max_length=25)	
	descricao = models.CharField(max_length=25)
	valor_atividade = models.FloatField(null=True)	
	evento = models.ForeignKey('Evento',related_name='minhas_atividades',default='')
	tipoAtividade = EnumField(TipoAtividade,max_length=25,default=TipoAtividade.DEFAULT)	
	
class Evento(models.Model):
	nome_evento = models.CharField(max_length=25)
	instituicao = models.ManyToManyField('instituicao.Instituicao')
	usuario_criador = models.ForeignKey('auth.User',related_name='meus_eventos',default='')	
	status = EnumField(TipoEvento,max_length=25,default=TipoEvento.NOVO)

	def inscricoes_pagas(self):
		inscricoes = self.minhas_inscricoes.get_queryset()
		return inscricoes.filter(meu_pagamento__pago=True)


class Cupom(models.Model):
	desconto = models.IntegerField()
	evento = models.ForeignKey('Evento',related_name='meus_cupons',default='')	
	
