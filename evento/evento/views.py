from django.shortcuts import render,redirect
from django.views import View
from appweb.forms.cadastroUsuarioForm import UsuarioForm
from appweb.forms.cadastroEventoForm import EventoForm
from appweb.forms.cadastroAtividadeForm import AtividadeForm
from appweb.forms.cadastroCupomForm import CupomForm
from appweb.forms.cadastroAtividadeForm import AtividadeForm,ResponsavelForm
from appweb.forms.associarEventoForm import FormEventoAssociado

class CadastroAtividade(View):
	atividade_form = AtividadeForm
	responsavel_form = ResponsavelForm
	def get(self, request, *args, **kwargs):
		atividade_form = self.atividade_form(user=self.request.user)
		responsavel_form = self.responsavel_form()
		context = { 'atividade_form': atividade_form, 'responsavel_form' : responsavel_form}
		return render(request, 'appweb/atividadeForm.html', context)

	def post(self, request, *args, **kwargs):		
		atividade_form = self.atividade_form(request.POST, user=self.request.user)
		responsavel_form = self.responsavel_form(request.POST)		
		if atividade_form.is_valid():
			if responsavel_form.is_valid():
				atividade = atividade_form.save(commit = False)
				responsavel = responsavel_form.save()
				atividade.responsavel = responsavel 	
				atividade.usuario_criador = self.request.user							
				atividade.save()
				return redirect('home')

class cadastroCupom(View):
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

class cadastroEvento(View):
	form = EventoForm
	def post(self, request, *args, **kwargs):	
		form = self.form(request.POST)
		if form.is_valid():
			evento = form.save(commit = False) 					
			evento.usuario_criador = request.user
			evento.save()
			return redirect('home')			
	def get(self, request, *args, **kwargs):
		form = self.form()
		return render(request, 'appweb/form.html', {'form': form})

class associarEvento(View):
	form = FormEventoAssociado
	def post(self,request, *args, **kwargs):
		form = self.form(request.POST)
		if form.is_valid():
			evento = form.save()

	def get(self, request, *args, **kwargs):
		form = self.form(user=self.request.user)
		return render(request, 'appweb/form.html', {'form': form})


	