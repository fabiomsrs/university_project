from django.shortcuts import render, redirect
from django.views import View
from appweb.forms.cadastroCupomForm import CupomForm
from django.template.context import RequestContext
from cupom.models import Cupom

# Create your views here.

class cadastroCupom(View):
	form = CupomForm
	def get(self, request, *args, **kwargs):		
		form = self.form(user=self.request.user)
		return render(request, 'appweb/cadastroCupom.html', {'form': form})

	def post(self, request, *args, **kwargs):			
		form = self.form(request.POST, user=self.request.user)		
		if form.is_valid():
			cupom = form.save(commit = False) 								
			cupom.save()
			return redirect('home')		
