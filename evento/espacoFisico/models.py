from django.db import models

# Create your models here.
class EspacoFisico(models.Model):
	nome_espaco_fisico = models.CharField(max_length=25)
	espaco_fisico = models.ManyToManyField('EspacoFisico',related_name='meus_espacos_fisicos')

	def associar_espacos(self, espaco_fisico):
		self.espaco_fisico =  espaco_fisico
