from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from appweb.forms.adicionarTag import AddTagUsuario, AddTagEvento
from core.models import Evento
# Create your views here.
class adicionarTagUsuario(View):
	form = AddTagUsuario
	def post(self, request, *args, **kwargs):			
		form = self.form(request.POST)			
		if form.is_valid():
			tag_usuario = form.save(commit=False)
			tag_usuario.save()
			tag_usuario.usuario.add(request.user)						
			return redirect('home')			
	def get(self, request, *args, **kwargs):				
		form = self.form()
		return render(request, 'appweb/form.html', {'form': form})

class adicionarTagEvento(View):
	form = AddTagEvento 
	def post(self, request, *args, **kwargs):	
		evento = get_object_or_404(Evento, pk=self.kwargs["pk"])	
		form = self.form(request.POST)
		print(request.POST,"\n\n",form.errors)		
		if form.is_valid():			
			tag = form.save(commit=False)									
			tag.save()
			tag.evento.add(evento)
			return redirect('evento:evento', pk=self.kwargs["pk"])				
	def get(self, request, *args, **kwargs):		
		form = self.form()
		return render(request, 'appweb/form.html', {'form': form})