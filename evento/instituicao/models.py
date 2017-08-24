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
	uf = models.CharField(max_length=2)
	evento = models.ManyToManyField('evento.Evento', through='Associacao')

	

	def __str__(self):
		return self.nome_instituicao

class Associacao(models.Model):
	evento = models.ForeignKey('evento.Evento')
	instituicao = models.ForeignKey('Instituicao')
	tipo_associacao = EnumField(TipoAssociacao,max_length=25,default=TipoAssociacao.DEFAULT)


