from django import forms
from evento.models import Evento

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		exclude = ['usuario_criador']
		fields = ('nome_evento','usuario_criador','status','tipo_evento')
