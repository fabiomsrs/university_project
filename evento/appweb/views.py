from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#
#
from .forms.cadastroUsuarioForm import UsuarioForm
from .forms.cadastroEventoForm import EventoForm
from .forms.cadastroAtividadeForm import AtividadeForm

# Create your views here.
def index(request):	
	if request.method == "POST":#TODO
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return HttpResponse("<h1>LOGIN ERROR</h1>")

	else:		
		form = AuthenticationForm()
		return render(request, "appweb/index.html", {'form':form})

def logout(request):
	logout(request)

def home(request):
	return render(request,"appweb/home.html")	

def cadastroUsuario(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			usuario = form.save(commit = False) 					
			usuario.save()
			return redirect('login')
		else:
			return HttpResponse("<h1>CADASTRO INVALIDO</h1>")
	else:
		form = UsuarioForm()
		return render(request, 'appweb/cadastroUsuario.html', {'form': form})

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
	