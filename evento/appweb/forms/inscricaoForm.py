import json
from django import forms
from evento.models import Evento, Atividade
from inscricao.models import Inscricao

class InscricaoForm(forms.ModelForm):	
	def __init__(self, *args, **kwargs):
		self.atividades = kwargs.pop("atividades")
		super(InscricaoForm, self).__init__(*args, **kwargs)	
		self.fields['atividade'].widget = forms.CheckboxSelectMultiple()
			
	class Meta:
		model = Inscricao		
		fields = ('evento','atividade')			