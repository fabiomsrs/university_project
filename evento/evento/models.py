from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

from enumfields import EnumField
from enumfields import Enum
from unittest.util import _MAX_LENGTH
from django.template.defaultfilters import default
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
	usuario_criador = models.ForeignKey('auth.User',related_name='minhas_atividades',default='')	
	evento = models.ForeignKey('Evento',related_name='minhas_atividades',default='')
	tipo_atividade = EnumField(TipoAtividade,max_length=25,default=TipoAtividade.DEFAULT)
	local = models.CharField(max_length=100)
	ispadrao = models.BooleanField()
	responsavel = models.ForeignKey('Responsavel', related_name='minhas_atividades', default = '')

	def get_descricao(self):
		return self.descricao

	def get_usuario(self):
		return self.usuario_criador

	def get_valor_atividade(self):
		return self.valor_atividade

	def get_evento(self):
		return self.evento

	def get_responsavel(self):
		return self.responsavel

	def __str__(self):
		return self.nome_atividade
	
class Evento(models.Model):
	nome_evento = models.CharField(max_length=25)	
	membros = models.ManyToManyField('auth.User',related_name='meus_eventos')
	status = EnumField(StatusEvento,max_length=25,default=StatusEvento.NOVO)
	tipo_evento = EnumField(TipoEvento,max_length=25,default = '')
	evento_principal = models.ForeignKey('Evento', related_name = 'meus_eventos_satelites',null=True)
	

	def get_tipo_evento(self):
		return self.tipo_evento
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

class CheckIn(models.Model):
	organizador = models.CharField(max_length=45)
	inscricao = models.ForeignKey('inscricao.RelacionamentoAtividadeInscricao',null=True)

	def get_organizador(self):
		return self.organizador


class Responsavel(models.Model):
	nome_responsavel = models.CharField(max_length=45)
	descricao_responsavel = models.CharField(max_length=250)

	def get_descricao(self):
		return self.descricao_responsavel

	def __str__(self):
		return self.nome_responsavel

class Cupom(models.Model):
	nome_cupom = models.CharField(max_length=50)
	desconto = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
	evento = models.ForeignKey('Evento',related_name='meus_cupons',default='')
	isautomatico = models.BooleanField()
	data_de_inicio = models.DateTimeField()
	data_de_fim = models.DateTimeField()

	def get_periodo(self):
		return data_de_fim - data_de_fim

	def __str__(self):
		return self.nome_cupom