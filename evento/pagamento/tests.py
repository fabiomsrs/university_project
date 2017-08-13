from django.test import TestCase
from django.contrib.auth.models import User

from inscricao.models import Inscricao, RelacionamentoAtividadeInscricao
from evento.models import Evento,Atividade
from pagamento.models import Pagamento

# Create your tests here.

class ModelTeste(TestCase):
	
	def test_payment(self):
		user = User.objects.create(username="user_teste",password="123")
		user.save()
		evento = Evento(nome_evento="teste_teste", usuario_criador=user)
		evento.save()
		atividade0 = Atividade(nome_atividade="teste", evento=evento, valor_atividade=10,descricao=" ")
		atividade0.save()
		atividade1 = Atividade(nome_atividade="teste1", evento=evento, valor_atividade=10,descricao=" ")
		atividade1.save()
		inscricao = Inscricao(usuario=user,evento=evento)
		inscricao.save()
		r = RelacionamentoAtividadeInscricao(atividade = atividade0, inscricao=inscricao)
		r.save()
		r1 = RelacionamentoAtividadeInscricao(atividade = atividade1, inscricao=inscricao)
		r1.save()
		inscricao.relacionamentoatividadeinscricao_set.set([r,r1])
		Pagamento(inscricao=inscricao).save()

		self.assertIs(inscricao.meu_pagamento.get_valor_total() > 0, True)
		self.assertEqual(inscricao.meu_pagamento.get_valor_total(), 20)		