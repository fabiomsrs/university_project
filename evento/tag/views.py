from django.shortcuts import render,redirect
from django.views import View
from appweb.forms.adicionarTag import AddTagUsuario, AddTagEvento
# Create your views here.
class adicionarTagUsuario(View):
	form = AddTagUsuario
	def post(self, request, *args, **kwargs):		
		form = self.form(request.POST)			
		if form.is_valid():
			tag_usuario = form.save(commit=False)
			tag_usuario.save()
			tag_usuario.usuario.add(request.user)
			form.save_m2m()						
			return redirect('home')			
	def get(self, request, *args, **kwargs):				
		form = self.form()
		return render(request, 'appweb/form.html', {'form': form})

class adicionarTagEvento(View):
	form = AddTagEvento 
	def post(self, request, *args, **kwargs):		
		form = self.form(request.POST, user=self.request.user)
		print(request.POST,"\n\n",form.errors)		
		if form.is_valid():
			form.save()						
			return redirect('home')				
	def get(self, request, *args, **kwargs):		
		form = self.form(user=self.request.user)
		return render(request, 'appweb/form.html', {'form': form})