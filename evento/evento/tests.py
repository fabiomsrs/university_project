from django.test import TestCase
from django.contrib.auth.models import User
import datetime
from cupom.models import Cupom
from evento.models import Evento,Atividade,Responsavel
from espacoFisico.models import EspacoFisico
# Create your tests here.

class CupomTest(TestCase):

	def test_valor_cupom_automatico(self):
		pass


	def test_periodo_cupom_automatico(self):		
		pass
		#self.assertIs(cupom.get_periodo() > 0, True) #TODO

class EventoTest(TestCase):

	def test_set_evento_principal(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste")		
		evento.save()
		evento.membros.add(user)
		evento1 = Evento(nome_evento="teste_teste1")
		evento1.save()
		evento1.membros.add(user)

		self.assertIs(evento1.set_evento_principal(evento), True)			

		with self.assertRaises(Exception):
			evento1.set_evento_principal(evento)

		with self.assertRaises(Exception):
			evento.set_evento_principal(evento1)
		
		

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
		responsavel = Responsavel(nome_responsavel="responsavel teste",descricao_responsavel="descricao")
		responsavel.save()		
		local = EspacoFisico(nome_espaco_fisico="espaco teste")
		local.save()
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=10),hora_fim=datetime.time(hour=15),local=local)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento1, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=10),hora_fim=datetime.time(hour=15),local=local)
		atividade1.save()
		self.assertEqual(evento.get_todas_atividades().count(),2)

class AtividadeTest(TestCase):
	def set_atividades_proibidas(self):
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
		local = EspacoFisico(nome_espaco_fisico="espaco teste")
		local.save()		
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=10),hora_fim=datetime.time(hour=15),local=local)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento1, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=10),hora_fim=datetime.time(hour=15),local=local)
		atividade1.save()
		atividade1.set_atividades_proibidas()		
		self.assertEqual(atividade1.atividades_proibidas,[atividade0])
		atividade2 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=10),hora_fim=datetime.time(hour=15),local=local)
		atividade2.save()
		atividade3 = Atividade(nome_atividade="teste1", evento=evento1, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=16),hora_fim=datetime.time(hour=15),local=local)
		atividade3.save()
		atividade3.set_atividades_proibidas()
		self.assertEqual(atividade3.atividades_proibidas,[])



	def checar_concomitancia(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste")
		evento.save()
		evento.membros.add(user)
		responsavel = Responsavel(nome_responsavel='responsavel teste',descricao_responsavel='descricao')
		responsavel.save()
		local = EspacoFisico(nome_espaco_fisico="espaco teste")
		local.save()	
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=10),hora_fim=datetime.time(hour=15),local=local)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento1, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,data_inicio=datetime.date(2005,1,1),data_de_fim=datetime.date(2005,1,1),hora_inicio=datetime.time(hour=10),hora_fim=datetime.time(hour=15),local=local)
		atividade1.save()
		atividade0.atividades_proibidas.add(atividade1)
		self.assertIs(atividade0.checar_concomitancia(atividade1), False)