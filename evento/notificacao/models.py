from django.db import models
from core.models import Evento

# Create your models here.
class GerenciadorDeNotificacoes:
	def __init__(self):
		self.evento = Evento.objects.all()
		self.usuario = []

