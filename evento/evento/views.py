from django.shortcuts import render,redirect

from appweb.forms.cadastroUsuarioForm import UsuarioForm
from appweb.forms.cadastroEventoForm import EventoForm
from appweb.forms.cadastroAtividadeForm import AtividadeForm
from appweb.forms.cadastroCupomForm import CupomForm

def cadastro_atividade(request):
	user = request.user
	if request.method == "POST":		
		form = AtividadeForm(request.POST, user=user)		
		if form.is_valid():
			atividade = form.save(commit = False) 								
			atividade.save()
			return redirect('home')			
	else:		
		form = AtividadeForm(user=user)
		return render(request, 'appweb/form.html', {'form': form})

def cadastroCupom(request):
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
		return render(request, 'appweb/form.html', {'form': form})