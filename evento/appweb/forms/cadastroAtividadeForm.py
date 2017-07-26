from django import forms
from evento.models import Atividade

class EventoForm(forms.ModelForm):
	class Meta:
		model = Atividade
		fields = ('nome_atividade','evento','descricao')
