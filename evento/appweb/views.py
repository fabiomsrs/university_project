from django.shortcuts import render,redirect
#
#
from .forms.cadastroUsuarioForm import UsuarioForm
from usuario.models import Usuario
# Create your views here.
def index(request):
	return render(request, "appweb/index.html",{})

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
	