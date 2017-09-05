from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from appweb.forms.inscricaoForm import InscricaoForm
from appweb.forms.cadastroCupomForm import CupomForm
from core.models import Evento,Atividade
from inscricao.models import Cupom,Pagamento,Inscricao

# Create your views here.
class Inscrever(View):
	form = InscricaoForm

	def post(self, request, *args, **kwargs):		
		form = self.form(data=request.POST, atividades=Atividade.objects.all())											
		evento = evento = get_object_or_404(Evento, pk=self.kwargs["pk"])														
		if form.is_valid():
			inscricao = Inscricao(usuario=request.user,evento=evento)	
			inscricao.save()	
			for atividade in request.POST.getlist('atividades'):
				atividade = Atividade.objects.get(pk=int(atividade))				
				inscricao.atividades.add(atividade)
			Pagamento(inscricao=inscricao).save()
			return redirect('evento:lista_outros_eventos')
							
	def get(self, request, *args, **kwargs):
		evento = get_object_or_404(Evento, pk=self.kwargs["pk"])		
		form = self.form(atividades=Atividade.objects.filter(evento=evento))													
		return render(request, 'appweb/inscricaoForm.html', {'form':form})


class CadastroCupom(View):
	form = CupomForm
	def get(self, request, *args, **kwargs):		
		form = self.form(user=self.request.user)
		return render(request, 'appweb/cadastroCupom.html', {'form': form})

	def post(self, request, *args, **kwargs):	
		evento = get_object_or_404(Evento, pk=self.kwargs["pk"])		
		form = self.form(request.POST, user=self.request.user)		
		if form.is_valid():
			cupom = form.save(commit = False)
			cupom.evento = evento 								
			cupom.save()
			return redirect('evento:evento', pk=self.kwargs["pk"])	