from django import forms
from django.forms import extras
from evento.models import Evento


class EventoForm(forms.ModelForm):
	inscricao_direta = forms.BooleanField(required=False)
	
	class Meta:
		model = Evento
		exclude = ['membros','evento_principal','data_inicio','data_de_fim']
		fields = '__all__'
