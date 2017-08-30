import json
from django import forms
from evento.models import Evento, Atividade
from inscricao.models import Inscricao

class InscricaoForm(forms.Form):	
	atividade = forms.CheckboxSelectMultiple()
	evento = forms.ChoiceField()
	def __init__(self, *args, **kwargs):
		self.atividades = kwargs.pop("atividades")
		super(InscricaoForm, self).__init__(*args, **kwargs)			
	