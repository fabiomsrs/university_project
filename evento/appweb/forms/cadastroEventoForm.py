from django import forms
from django.forms import extras
from evento.models import Evento


class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		exclude = ['membros','evento_principal','data_inicio','data_de_fim','hora_inicio','hora_fim']
		fields = '__all__'
