from django.test import TestCase
from evento.models import Cupom
# Create your tests here.

class CupomTest(TestCase):

	def test_valor_cupom_automatico(self):
		pass


	def test_periodo_cupom_automatico(self):		
		self.assertIs(cupom.get_periodo() > 0, True) #TODO

class EventoTest(TestCase):

	def test_evento_satelite(self):
		pass #evento satelite nao pode ser principal