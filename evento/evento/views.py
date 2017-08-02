from django.shortcuts import render,redirect

from appweb.forms.cadastroUsuarioForm import UsuarioForm
from appweb.forms.cadastroEventoForm import EventoForm
from appweb.forms.cadastroAtividadeForm import AtividadeForm

def cadastroAtividade(request):
	if request.method == "POST":		
		form = AtividadeForm(request.POST)		
		if form.is_valid():
			atividade = form.save(commit = False) 								
			atividade.save()
			return redirect('home')			
	else:
		form = AtividadeForm(request=request)
		return render(request, 'appweb/cadastroAtividade.html', {'form': form})

def cadastroEvento(request):
	if request.method == "POST":
		form = EventoForm(request.POST)
		if form.is_valid():
			evento = form.save(commit = False) 					
			evento.usuario_criador = request.user
			evento.save()
			return redirect('home')			
	else:
		form = EventoForm()
		return render(request, 'appweb/cadastroEvento.html', {'form': form})