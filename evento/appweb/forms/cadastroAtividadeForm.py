from django import forms
from evento.models import Atividade

class AtividadeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop("request")
		super(AtividadeForm, self).__init__(*args, **kwargs)		
	
		self.fields['evento'].queryset =  self.request.user.meus_eventos.all()
		self.fields['evento'].empty_label = 'Empty'			
		self.fields['evento'].label = 'Evento pertencente'

	class Meta:
		model = Atividade		
		fields = ('nome_atividade','evento','descricao')				