from django.shortcuts import render,redirect
from django.views import View
from appweb.forms.cadastroUsuarioForm import UsuarioForm
from appweb.forms.cadastroEventoForm import EventoForm
from appweb.forms.cadastroAtividadeForm import AtividadeForm
from appweb.forms.cadastroCupomForm import CupomForm

class CadastroAtividade(View):
	form = AtividadeForm

	def get(self, request, *args, **kwargs):
		form = self.form(user=self.request.user)
		return render(request, 'appweb/form.html', {'form': form})

	def post(self, request, *args, **kwargs):		
		form = self.form(request.POST, user=self.request.user)		
		if form.is_valid():
			atividade = form.save(commit = False) 								
			atividade.save()
			return redirect('home')			

class cadastroCupom(View):
	def get(self, request, *args, **kwargs):		
		form = CupomForm(user=self.request.user)
		return render(request, 'appweb/cadastroCupom.html', {'form': form})

	def post(self, request, *args, **kwargs):			
		form = CupomForm(request.POST, user=self.request.user)		
		if form.is_valid():
			cupom = form.save(commit = False) 								
			cupom.save()
			return redirect('home')		

class cadastroEvento(View):
	def post(self, request, *args, **kwargs):	
		form = EventoForm(request.POST)
		if form.is_valid():
			evento = form.save(commit = False) 					
			evento.usuario_criador = request.user
			evento.save()
			return redirect('home')			
	def get(self, request, *args, **kwargs):
		form = EventoForm()
		return render(request, 'appweb/form.html', {'form': form})