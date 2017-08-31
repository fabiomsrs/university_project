from django.shortcuts import render,redirect
from django.views import View
from appweb.forms.inscricaoForm import InscricaoForm
from appweb.forms.cadastroCupomForm import CupomForm
from core.models import Evento,Atividade
from inscricao.models import ItemInscricao,Cupom,Pagamento

# Create your views here.
class Inscricao(View):
	form = InscricaoForm

	def post(self, request, *args, **kwargs):		
		form = self.form(request.POST, atividades=Atividade.objects.all())
		print(form.errors,"\n\n",request.POST,"\n\n")						
		if form.is_valid():
			inscricao = form.save(commit = False)
			inscricao.usuario = request.user
			inscricao.save()
			for atividade in request.POST['atividade']:				
				ItemInscricao(atividade=Atividade.objects.get(pk=int(atividade)),inscricao=inscricao).save()
			Pagamento(inscricao=inscricao).save()
			return redirect('home')

	def get(self, request, *args, **kwargs):		
		form = self.form(atividades=Atividade.objects.all())	
		lista_atividade = {}		

		for atividade in Atividade.objects.all():
			if atividade.evento.nome_evento in lista_atividade:
					lista_atividade[atividade.evento.nome_evento].append(atividade.nome_atividade)
			else:
				if atividade.ispadrao == False:
					lista_atividade[atividade.evento.nome_evento] = [atividade.nome_atividade]

		eventos = [str(evento) for evento in Evento.objects.all()]	
		context = {'eventos':eventos,'atividades_por_evento':lista_atividade, 'form':form}						
		return render(request, 'appweb/inscricaoForm.html', context)


class CadastroCupom(View):
	form = CupomForm
	def get(self, request, *args, **kwargs):		
		form = self.form(user=self.request.user)
		return render(request, 'appweb/cadastroCupom.html', {'form': form})

	def post(self, request, *args, **kwargs):			
		form = self.form(request.POST, user=self.request.user)		
		if form.is_valid():
			cupom = form.save(commit = False) 								
			cupom.save()
			return redirect('home')	