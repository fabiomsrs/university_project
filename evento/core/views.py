from django.shortcuts import render,redirect, render_to_response,get_object_or_404
from django.views import View
from appweb.forms.cadastroUsuarioForm import UsuarioForm
from appweb.forms.cadastroEventoForm import EventoForm
from appweb.forms.cadastroAtividadeForm import AtividadeForm
from appweb.forms.criarEquipeForm import EquipeForm
from django.template.context import RequestContext
from appweb.forms.cadastroAtividadeForm import AtividadeForm,ResponsavelForm
from appweb.forms.associarEventoForm import FormEventoPrincipal
from core.models import Evento
from django.template.context_processors import request


class CadastroAtividade(View):	
	atividade_form = AtividadeForm
	responsavel_form = ResponsavelForm
	def get(self, request, *args, **kwargs):		
		atividade_form = self.atividade_form()
		responsavel_form = self.responsavel_form()
		context = { 'atividade_form': atividade_form, 'responsavel_form' : responsavel_form}
		return render(request, 'appweb/atividadeForm.html', context)

	def post(self, request, *args, **kwargs):		
		evento = get_object_or_404(Evento, pk=self.kwargs["pk"])		
		atividade_form = self.atividade_form(request.POST)
		responsavel_form = self.responsavel_form(request.POST)		
		if atividade_form.is_valid():
			if responsavel_form.is_valid():
				atividade = atividade_form.save(commit = False)
				responsavel = responsavel_form.save()				
				atividade.responsavel = responsavel 
				atividade.evento = evento	
				atividade.usuario_criador = self.request.user							
				atividade.save()
				return redirect('evento:evento', pk=self.kwargs["pk"])


class MeusEventos(View):
	def get(self, request, *args, **kwargs):		
		eventos = request.user.meus_eventos.all()
		return render(request, 'appweb/meusEventos.html', {'eventos':eventos})


class Inscrever(View):
	def get(self, request, *args, **kwargs):				
		user = request.user
		eventos = Evento.objects.all().exclude(membros=user)
		return render(request, 'appweb/eventos.html', {'eventos':eventos})


class EventoEspecifico(View):	
	def get(self, request, *args, **kwargs):
		evento = get_object_or_404(Evento, pk=self.kwargs["pk"])
		return render(request, 'appweb/eventoHome.html', {'evento':evento})


class CadastroEvento(View):
	form = EventoForm
	def post(self, request, *args, **kwargs):		
		form = self.form(request.POST)
		print(form.errors)
		if form.is_valid():
			evento = form.save() 					
			evento.membros.add(request.user)			
			return redirect('home')			
	def get(self, request, *args, **kwargs):
		form = self.form()
		return render(request, 'appweb/form.html', {'form': form})


class AssociarEvento(View):	
	form_evento_principal = FormEventoPrincipal	
	def post(self,request, *args, **kwargs):	
		evento = get_object_or_404(Evento, pk=self.kwargs["pk"])													
		evento.save()
		return redirect('evento:evento', pk=self.kwargs["pk"])					

	def get(self, request, *args, **kwargs):
		evento = get_object_or_404(Evento, pk=self.kwargs["pk"])
		eventos = Evento.objects.all().exclude(pk=evento.pk)
		form_evento_principal = self.form_evento_principal(eventos=eventos)		
		context = {'form_evento_principal':form_evento_principal, 'eventos':eventos, 'evento':evento}
		return render(request, 'appweb/associarEvento.html', context)
		

class CriarEquipe(View):
	form = EquipeForm
		
	def post(self, request, *args, **kwargs):
		form = self.form(request.POST)

		if form.is_valid():
			equipe = form.save()
			
	def get(self, request, *args, **kwargs):
		form = EquipeForm
		return render_to_response(request, 'appweb/criaEquipe.html', {'form': form})