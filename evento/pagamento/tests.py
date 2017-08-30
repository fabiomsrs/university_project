from django.test import TestCase
from django.contrib.auth.models import User
from inscricao.models import Inscricao, RelacionamentoAtividadeInscricao
from evento.models import Evento,Atividade,Responsavel
from pagamento.models import Pagamento

# Create your tests here.

class ModelTeste(TestCase):
	
	def test_payment(self):
		user = User.objects.create(username="user_teste2",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste2")
		evento.save()
		evento.membros.add(user)
		responsavel =  Responsavel(nome_responsavel='responsavel teste',descricao_responsavel='descricao')
		responsavel.save()
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user)
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento, valor_atividade=10,descricao=" ",ispadrao=False,responsavel=responsavel,usuario_criador=user)
		atividade1.save()
		inscricao = Inscricao(usuario=user,evento=evento)
		inscricao.save()
		r = RelacionamentoAtividadeInscricao(atividade = atividade0, inscricao=inscricao)
		r.save()
		r1 = RelacionamentoAtividadeInscricao(atividade = atividade1, inscricao=inscricao)
		r1.save()
		inscricao.relacionamentoatividadeinscricao_set.set([r,r1])
		Pagamento(inscricao=inscricao).save()

		self.assertIs(inscricao.meu_pagamento.calcular_valor_total() > 0, True)
		self.assertEqual(inscricao.meu_pagamento.calcular_valor_total(), 20)		