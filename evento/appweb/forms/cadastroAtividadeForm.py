from django import forms
from evento.models import Atividade

class EventoForm(forms.ModelForm):
	class Meta:
		model = Atividade
		fields = ('nomeAtividade','evento','descricao')
