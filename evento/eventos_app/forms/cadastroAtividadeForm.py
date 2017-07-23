from django import forms
from ..models import Atividade #Mudar Import

class EventoForm(forms.ModelForm):
	class Meta:
		model = Atividade
		fields = ('nomeAtividade','evento','descricao')
