from django.test import TestCase
from evento.models import Cupom
# Create your tests here.

class CupomTest(TestCase):

	def test_valor_cupom_automatico(self):
		pass


	def test_periodo_cupom_automatico(self):		
		pass
		#self.assertIs(cupom.get_periodo() > 0, True) #TODO

class EventoTest(TestCase):

	def test_evento_satelite(self):
		pass #evento satelite nao pode ser principal

class ConcomitanciaAtividade(TestCase):
	def checar_concomitancia(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste", usuario_criador=user)
		evento.save()
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ")
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento, valor_atividade=10,descricao=" ")
		atividade1.save()
		atividade0.atividades_proibidas.add(atividade1)
		self.assertIs(atividade0.checar_concomitancia(atividade1), False)