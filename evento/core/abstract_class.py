from django.db import models
from inscricao.models import Inscricao,ItemInscricao

class StatusEvento(models.Model):
	pass


class Novo(StatusEvento):
	
	def inscrever(self, user, atividades):						
		return "Inscricoes ainda nao foram abertas"
	class Meta:
		abstract = True


class EmAndamento(StatusEvento):
	
	def inscrever(self, user, atividades):					
		return "Inscricoes encerradas"

	class Meta:
		abstract = True


class InscricoesAbertas(StatusEvento):

	def inscrever(self, user, atividades):
		inscricao = Inscricao.objects.create(usuario=user,evento=self.evento)
		for atividade in atividades:
			ItemInscricao.objects.create(inscricao=inscricao,atividade=atividade)
					
		return [item.atividade for item in inscricao.meus_itens.all()]

	class Meta:
		abstract = True
