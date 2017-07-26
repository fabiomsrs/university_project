from django.db import models

# Create your models here.
class Inscricao(models.Model):	
	usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='minhas_inscricoes')	
	evento = models.ForeignKey('evento.Evento', on_delete=models.CASCADE, related_name='minhas_inscricoes')
	atividade = models.ManyToManyField('evento.Atividade', through='RelacionamentoAtividadeInscricao')
		
class RelacionamentoAtividadeInscricao(models.Model):
	atividade = models.ForeignKey('evento.Atividade')
	inscricao = models.ForeignKey('Inscricao')