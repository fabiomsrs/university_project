from django.db import models

# Create your models here.
class Inscricao(models.Model):	
	usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='minhas_inscricoes')	
	evento = models.ForeignKey('evento.Evento', on_delete=models.CASCADE, related_name='minhas_inscricoes')
	atividade = models.ManyToManyField('evento.Atividade', through='RelacionamentoAtividadeInscricao')

	def __str__(self):
		return self.usuario.first_name

class RelacionamentoAtividadeInscricao(models.Model):
	atividade = models.ForeignKey('evento.Atividade')
	inscricao = models.ForeignKey('Inscricao')