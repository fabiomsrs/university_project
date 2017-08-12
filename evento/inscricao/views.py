from django.shortcuts import render
from django.views import View
from appweb.forms.inscricaoForm import InscricaoForm
# Create your views here.
class Inscricao(View):
	form = InscricaoForm

	def post(self, request, *args, **kwargs):		
		form = self.form(request.POST)		
		if form.is_valid():
			inscricao = form.save(commit = False) 								
			inscricao.save()
			return redirect('home')		

	def get(self, request, *args, **kwargs):
		form = self.form()		
		return render(request, 'appweb/ajaxForm.html', {'form': form})		