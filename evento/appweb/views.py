from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#
#
from .forms.cadastroUsuarioForm import UsuarioForm

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
		form = UsuarioForm()
		return render(request, 'appweb/cadastroUsuario.html', {'form': form})
	