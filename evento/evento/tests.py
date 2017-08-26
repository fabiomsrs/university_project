from django.test import TestCase
from django.contrib.auth.models import User
from cupom.models import Cupom
from evento.models import Evento,Atividade,Responsavel
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

	def test_inscricoes_pagas(self):
		user = User.objects.create(username="user_teste1",password="123")
		user.save()
		evento = Evento(id=1, nome_evento="teste_teste1")		
		evento.save()
		evento.membros.add(user)
		self.assertEqual(evento.get_inscricoes_pagas(), "nenhuma inscricao paga")

	def test_get_todas_atividades(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste")		
		evento.save()
		evento.membros.add(user)
		evento1 = Evento(nome_evento="teste_teste1",evento_principal=evento)
		evento1.save()
		evento1.membros.add(user)		
		responsavel = Responsavel(nome_responsavel='responsavel teste',descricao_responsavel='descricao')
		responsavel.save()
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento1, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user)
		atividade1.save()		
		self.assertEqual(evento.get_todas_atividades().count(),2)

class ConcomitanciaAtividade(TestCase):
	def checar_concomitancia(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste")
		evento.save()
		evento.membros.add(user)
		responsavel = Responsavel(nome_responsavel='responsavel teste',descricao_responsavel='descricao')
		responsavel.save()
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user)
		atividade1.save()
		atividade0.atividades_proibidas.add(atividade1)
		self.assertIs(atividade0.checar_concomitancia(atividade1), False)