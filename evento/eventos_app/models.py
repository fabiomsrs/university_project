from django.db import models

class Usuario(models.Model):
	nomeUsuario = models.CharField(max_length=25)
	login = models.CharField(max_length=25)
	password = models.CharField(max_length=25)	

class Atividade(models.Model):
	nomeAtividade = models.CharField(max_length=25)	
	descricao = models.CharField(max_length=25)
	valorAtividade = models.FloatField()	
	evento = models.ForeignKey('Evento')

class Inscricao(models.Model):	
	usuario = models.ForeignKey('Usuario')	
	evento = models.ForeignKey('Evento')
	atividade = models.ManyToManyField('Atividade', through='RelacionamentoAtividadeInscricao')
		
	
class Cupom(models.Model):
	desconto = models.IntegerField()
	evento = models.ForeignKey('Evento')
	inscricao = models.ForeignKey('Inscricao')
	
class Evento(models.Model):
	nomeEvento = models.CharField(max_length=25)
	instituicao = models.ManyToManyField('Instituicao', through='Relacionamento')
	usuarioCriador = models.ForeignKey('Usuario')

class Instituicao(models.Model):
	nomeInstituicao = models.CharField(max_length=25)
	uf = models.CharField(max_length=2)
	#TODO listas de tags

class Relacionamento(models.Model):
	evento = models.ForeignKey('Evento')
	instituicao = models.ForeignKey('Instituicao')
	descricaoRelacionamento = models.CharField(max_length=25)

class RelacionamentoAtividadeInscricao(models.Model):
	atividade = models.ForeignKey('Atividade')
	inscricao = models.ForeignKey('Inscricao')
	
class Pagamento(models.Model):	
	valorTotal = models.FloatField(null=True)
	pago = models.BooleanField(default=False)	
	inscricao = models.ForeignKey('Inscricao')
	def getValorTotal(self):
		relacionamentos = RelacionamentoAtividadeInscricao.objects.filter(inscricao = self.inscricao)
		valorTotal = 0
		for i in relacionamentos:
			valorTotal += i.atividade.valorAtividade

		return valorTotal