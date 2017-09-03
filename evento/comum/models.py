from django.db import models
from enumfields import EnumField
from enumfields import Enum
# Create your models here.

class TipoAssociacao(Enum):
	PATROCINIO = 'patrocinio'
	APOIO = 'apoio'
	DEFAULT = 'default'

class Instituicao(models.Model):
	nome_instituicao = models.CharField(max_length=25)
	unidade_federativa = models.CharField(max_length=2)
	evento = models.ManyToManyField('core.Evento', through='Associacao')	

	def __str__(self):
		return self.nome_instituicao

class Associacao(models.Model):
	evento = models.ForeignKey('core.Evento')
	instituicao = models.ForeignKey('Instituicao')
	tipo_associacao = EnumField(TipoAssociacao,max_length=25,default=TipoAssociacao.DEFAULT)

class EspacoFisico(models.Model):
	nome_espaco_fisico = models.CharField(max_length=25)
	espaco_fisico = models.ManyToManyField('EspacoFisico',related_name='meus_espacos_fisicos')

	def associar_espacos(self, espaco_fisico):
		self.espaco_fisico =  espaco_fisico

class Tag(models.Model):
	nome_tag = models.CharField(max_length=25)
	class Meta:
		abstract = True

class TagUsuario(Tag):	
	usuario = models.ManyToManyField('auth.User')

class TagEvento(Tag):
	evento = models.ManyToManyField('core.Evento')