from django.shortcuts import render,redirect, render_to_response
from django.views import View
from appweb.forms.cadastroUsuarioForm import UsuarioForm
from appweb.forms.cadastroEventoForm import EventoForm
from appweb.forms.cadastroAtividadeForm import AtividadeForm
from appweb.forms.criarEquipeForm import EquipeForm
from django.template.context import RequestContext
from appweb.forms.cadastroAtividadeForm import AtividadeForm,ResponsavelForm
from appweb.forms.associarEventoForm import FormEventoPrincipal
from evento.models import Evento
from django.template.context_processors import request

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

class cadastroEvento(View):
	form = EventoForm
	def post(self, request, *args, **kwargs):	
		form = self.form(request.POST)
		if form.is_valid():
			evento = form.save() 					
			evento.membros.add(request.user)			
			return redirect('home')			
	def get(self, request, *args, **kwargs):
		form = self.form()
		return render(request, 'appweb/form.html', {'form': form})


class associarEvento(View):
	form_evento_principal = FormEventoPrincipal	

	def post(self,request, *args, **kwargs):						
		for evento in Evento.objects.all():
			if evento.nome_evento == request.POST['evento_satelite']:				
				evento.evento_principal = Evento.objects.get(pk=int(request.POST['evento_principal']))
				evento.save()
		return redirect('home')					

	def get(self, request, *args, **kwargs):
		evento_satelite = [str(evento) for evento in self.request.user.meus_eventos.all()]
		eventos = Evento.objects.all()
		form_evento_principal = self.form_evento_principal(eventos=eventos)		
		context = {'form_evento_principal':form_evento_principal, 'eventos':eventos, 'evento_satelite':evento_satelite}
		return render(request, 'appweb/associarEvento.html', context)
		
class criarEquipe(View):
	form = EquipeForm
		
	def post(self, request, *args, **kwargs):
		form = self.form(request.POST)

def cadastro_cupom(request):
	user = request.user
	print(request.POST,"\n\n")
	if request.method == "POST":				
		form = CupomForm(request.POST, user=user)		
		if form.is_valid():
			cupom = form.save(commit = False) 								
			cupom.save()
			return redirect('home')
		else:
			print('ERROOOOOOOR')
			print(request.POST,"\n\n")				
	else:		
		form = CupomForm(user=user)
		return render(request, 'appweb/cadastroCupom.html', {'form': form})

def cadastro_evento(request):
	if request.method == "POST":
		form = EventoForm(request.POST)
		if form.is_valid():
			equipe = form.save()
			
	def get(self, request, *args, **kwargs):
		form = EquipeForm
		return render_to_response(request, 'appweb/criaEquipe.html', {'form': form})