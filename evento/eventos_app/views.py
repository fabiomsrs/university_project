from django.shortcuts import render,redirect
#
#
from .forms.cadastroUsuarioForm import UsuarioForm
from .models import Usuario
# Create your views here.
def index(request):
	return render(request, "eventos_app/index.html",{})

def cadastroUsuario(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			usuario = form.save(commit = False) 					
			usuario.save()
			return redirect('login')

	else:
		form = UsuarioForm()
		return render(request, 'eventos_app/cadastroUsuario.html', {'form': form})
	