from django.db import models


class Atividade(models.Model):
	nomeAtividade = models.CharField(max_length=25)	
	descricao = models.CharField(max_length=25)
	valorAtividade = models.FloatField(null=True)	
	evento = models.ForeignKey('Evento')
		
	
class Cupom(models.Model):
	desconto = models.IntegerField()
	evento = models.ForeignKey('Evento')
	inscricao = models.ForeignKey('usuario.Inscricao',null=True)
	
class Evento(models.Model):
	nomeEvento = models.CharField(max_length=25)
	instituicao = models.ManyToManyField('Instituicao', through='Relacionamento')
	usuarioCriador = models.ForeignKey('usuario.Usuario',default='')

class Instituicao(models.Model):
	nomeInstituicao = models.CharField(max_length=25)
	uf = models.CharField(max_length=2)
	#TODO listas de tags

class Relacionamento(models.Model):
	evento = models.ForeignKey('Evento')
	instituicao = models.ForeignKey('Instituicao')
	descricaoRelacionamento = models.CharField(max_length=25)
	
class Pagamento(models.Model):	
	valorTotal = models.FloatField(null=True)
	pago = models.BooleanField(default=False)	
	inscricao = models.ForeignKey('usuario.Inscricao',default='')
	def getValorTotal(self):
		relacionamentos = RelacionamentoAtividadeInscricao.objects.filter(inscricao = self.inscricao)
		valorTotal = 0
		for i in relacionamentos:
			valorTotal += i.atividade.valorAtividade

		return valorTotal