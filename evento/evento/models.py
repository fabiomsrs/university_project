from django.db import models
from django.core.validators import MaxValueValidator

from enumfields import EnumField
from enumfields import Enum
# Create your models here.

class TipoEvento(Enum):
	CONGRESSO = 'congresso'
	SIMPOSIO = 'simposio'
	SEMANAS =  'semanas'
	OUTROS = ''
	
class StatusEvento(Enum):
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
	descricao = models.TextField(max_length=250)
	valor_atividade = models.FloatField(null=True)	
	evento = models.ForeignKey('Evento',related_name='minhas_atividades',default='')
	tipo_atividade = EnumField(TipoAtividade,max_length=25,default=TipoAtividade.DEFAULT)

	def get_descricao(self):
		return self.descricao

	def get_valor_atividade(self):
		return self.valor_atividade

	def get_evento():
		return self.evento

	def __str__(self):
		return self.nome_atividade
	
class Evento(models.Model):
	nome_evento = models.CharField(max_length=25)	
	usuario_criador = models.ForeignKey('auth.User',related_name='meus_eventos',default='')	
	status = EnumField(StatusEvento,max_length=25,default=StatusEvento.NOVO)

	def get_usuario(self):
		return self.usuario_criador

	def get_status(self):
		return self.status

	def get_inscricoes_pagas(self):
		inscricoes = self.minhas_inscricoes.get_queryset()
		return inscricoes.filter(meu_pagamento__pago=True)

	def get_meus_cupons(self):
		return self.meus_cupons.all()

	def get_minhas_tags(self):
		self.tagevento_set.all()

	def get_minhas_instituicoes(self):
		self.instituicao_set.all()


	def __str__(self):
		return self.nome_evento

class Cupom(models.Model):
	desconto = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
	evento = models.ForeignKey('Evento',related_name='meus_cupons',default='')	
	
