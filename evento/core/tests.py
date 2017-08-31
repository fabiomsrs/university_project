from django.test import TestCase
from django.contrib.auth.models import User
import datetime
from cupom.models import Cupom
from evento.models import Evento,Atividade,Responsavel,EventoInscrevivel
from espacoFisico.models import EspacoFisico
# Create your tests here.

class EventoTest(TestCase):
	def test_set_valor_total(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = EventoInscrevivel(nome_evento="teste_teste")		
		evento.save()
		evento.membros.add(user)		

		self.assertEqual(evento.set_valor_total(), "nenhuma atividade cadastrada")			
		
	
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
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento1, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade1.save()
		evento.set_todas_atividades()
		self.assertEqual(evento.minhas_atividades.all().count(),2)

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
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento1, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade1.save()
		atividade1.set_atividades_proibidas()		
		self.assertEqual(atividade1.atividades_proibidas,[atividade0])
		atividade2 = Atividade(nome_atividade="teste", evento=evento, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade2.save()
		atividade3 = Atividade(nome_atividade="teste1", evento=evento1, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=17),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=18),local=local)
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
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento1, valor=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade1.save()
		atividade0.atividades_proibidas.add(atividade1)
		self.assertIs(atividade0.checar_concomitancia(atividade1), False)