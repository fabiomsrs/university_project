from django import forms
from evento.models import Evento

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = ('nome_evento','usuario_criador')
