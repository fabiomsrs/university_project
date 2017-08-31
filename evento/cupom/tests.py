from django.test import TestCase
from django.contrib.auth.models import User
import datetime
from cupom.models import CupomAutomatico
from evento.models import Evento,Atividade,Responsavel,EventoInscrevivel
from espacoFisico.models import EspacoFisico
# Create your tests here.

class CupomTest(TestCase):

	def test_desconto_cupom_automatico(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste")		
		evento.save()		
		evento.membros.add(user)
		responsavel = Responsavel(nome_responsavel="responsavel teste",descricao_responsavel="descricao")
		responsavel.save()		
		local = EspacoFisico(nome_espaco_fisico="espaco teste")
		local.save()
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor=10,descricao=" ",tipo_atividade="simposio",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade0.save()		
		cupom = CupomAutomatico(nome_cupom='cupom',desconto=10,evento=evento)		
		self.assertEqual(cupom.descontar_valor_evento(), 9)
		
		evento1 = EventoInscrevivel(nome_evento="teste_teste",tipo_evento="congresso")		
		evento1.valor = 100
		evento1.save()		
		evento1.membros.add(user)
		atividade1 = Atividade(nome_atividade="teste", evento=evento1, valor=20,descricao=" ",tipo_atividade="simposio",ispadrao=False,responsavel=responsavel,usuario_criador=user,horario_inicio=datetime.datetime(year=2005,month=1,day=1,hour=15),horario_final=datetime.datetime(year=2005,month=1,day=1,hour=16),local=local)
		atividade1.save()
		cupom = CupomAutomatico(nome_cupom='cupom',desconto=10,evento=evento1)				
		cupom.descontar_valor_evento()
		self.assertEqual(cupom.descontar_valor_evento(),90)
	
	def test_periodo_cupom_automatico(self):		
		pass
		#self.assertIs(cupom.get_periodo() > 0, True) #TODO

