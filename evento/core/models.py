from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.template.defaultfilters import default
from enumfields import EnumField
from enumfields import Enum
from unittest.util import _MAX_LENGTH
from .managers import EventoSateliteManager
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


class Inscrevivel(models.Model):
	valor = models.FloatField(default=0)	
	class Meta:
		abstract = True

class Atividade(Inscrevivel):
	nome_atividade = models.CharField(max_length=25)	
	descricao = models.TextField(max_length=250)
	usuario_criador = models.ForeignKey('auth.User',related_name='minhas_atividades',default='')	
	evento = models.ForeignKey('Evento',related_name='minhas_atividades',default='')
	tipo_atividade = EnumField(TipoAtividade,max_length=25,default=TipoAtividade.DEFAULT)
	local = models.ForeignKey('comum.EspacoFisico', related_name='atividades',null=True)
	horario_inicio = models.DateField(null=True)
	horario_final = models.DateField(null=True)
	ispadrao = models.BooleanField()
	responsavel = models.ForeignKey('Responsavel', related_name='minhas_atividades', default = '')
	atividades_proibidas = models.ManyToManyField('Atividade')

	def set_atividades_proibidas(self):
		for atividade in Atividade.objects.all():
			if self.horario_inicio >= atividade.horario_inicio and self.horario_final <= atividade.horario_fim and self.local == atividade.local:				
				self.atividades_proibidas.add(atividade)							

	def checar_concomitancia(self, atividade):		
		if atividade in self.atividades_proibidas.all():
			return False 
		else:
			return True

	def __str__(self):
		return self.nome_atividade

	
class Evento(models.Model):
	nome_evento = models.CharField(max_length=25)	
	membros = models.ManyToManyField('auth.User',related_name='meus_eventos')
	status = EnumField(StatusEvento,max_length=25,default=StatusEvento.NOVO)
	tipo_evento = EnumField(TipoEvento,max_length=25,default = '')
	evento_principal = models.ForeignKey('Evento', related_name = 'meus_eventos_satelites',null=True)	
	data_inicio = models.DateField(null=True)	
	data_de_fim = models.DateField(null=True)	

	def set_evento_principal(self, evento):
		if self.evento_principal == None and evento.evento_principal == None:
			self.evento_principal = evento
			return True
		else:
			raise Exception("associcao error")

	def set_todas_atividades(self):		
		if self.meus_eventos_satelites.count != 0:			
			for evento_satelite in self.meus_eventos_satelites.all():
				for atividade in evento_satelite.minhas_atividades.all():
					self.minhas_atividades.add(atividade)
	
	def get_inscricoes_pagas(self):
		if self.minhas_inscricoes.count() != 0:
			inscricoes = self.minhas_inscricoes.get_queryset()
			return inscricoes.filter(meu_pagamento__pago=True)
		else:
			return "nenhuma inscricao paga"

	def __str__(self):
		return self.nome_evento

	objects = EventoSateliteManager()


class EventoInscrevivel(Evento,Inscrevivel):
	
	def set_valor_total(self):
		self.valor = 0
		if self.evento_ptr.minhas_atividades.count() != 0:
			for atividade in self.evento_ptr.minhas_atividades.all():
				self.valor += atividade.valor
		else:
			return "nenhuma atividade cadastrada"				
		


class Agenda(models.Model):
	evento = models.OneToOneField('Evento', related_name='minha_agenda')


class CheckIn(models.Model):
	organizador = models.CharField(max_length=45)
	inscricao = models.ForeignKey('inscricao.ItemInscricao',null=True)


class Responsavel(models.Model):
	nome_responsavel = models.CharField(max_length=45)
	descricao_responsavel = models.CharField(max_length=250)

	def __str__(self):
		return self.nome_responsavel


class Trilha(models.Model):
	nome = models.CharField(max_length=25)
	tema = models.CharField(max_length=25)
	atividades = models.ManyToManyField('Atividade')
	coordenadores = models.ManyToManyField('auth.User')
	

class Pacote(models.Model):
	nome_pacote = models.CharField(max_length=25)
	atividades = models.ManyToManyField('Atividade')
	valor_total = models.FloatField(null=True)