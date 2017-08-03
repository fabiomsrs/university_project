from django.shortcuts import render,redirect

from appweb.forms.adicionarTag import AddTagUsuario, AddTagEvento
# Create your views here.
def adicionar_tag_usuario(request):
	if request.method == "POST":		
		form = AddTagUsuario(request.POST)			
		if form.is_valid():
			tag_usuario = form.save()						
			return redirect('home')			
	else:		
		form = AddTagUsuario()
		return render(request, 'appweb/form.html', {'form': form})

def adicionar_tag_evento(request):
	user = request.user
	if request.method == "POST":		
		form = AddTagEvento(request.POST, user=user)
		print(request.POST,"\n\n",form.errors)		
		if form.is_valid():
			form.save()						
			return redirect('home')				
	else:		
		form = AddTagEvento(user=user)
		return render(request, 'appweb/form.html', {'form': form})