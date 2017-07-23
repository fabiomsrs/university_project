from django import forms
from ..models import Evento #Mudar Import

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = ('nomeEvento','usuarioCriador')
