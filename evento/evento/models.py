from django.db import models


class Atividade(models.Model):
	nome_atividade = models.CharField(max_length=25)	
	descricao = models.CharField(max_length=25)
	valor_atividade = models.FloatField(null=True)	
	evento = models.ForeignKey('Evento',related_name='minhas_atividades')
		
class Evento(models.Model):
	nome_evento = models.CharField(max_length=25)
	instituicao = models.ManyToManyField('instituicao.Instituicao')
	usuario_criador = models.ForeignKey('usuario.Usuario',related_name='meus_eventos',default='')

class Cupom(models.Model):
	desconto = models.IntegerField()
	evento = models.ForeignKey('Evento',related_name='meus_cupons',default='')	
	
