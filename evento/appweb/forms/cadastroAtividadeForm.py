from django import forms
from evento.models import Atividade

class AtividadeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user")
		super(AtividadeForm, self).__init__(*args, **kwargs)		
	
		self.fields['evento'].queryset =  self.user.meus_eventos.all()
		self.fields['evento'].empty_label = 'Empty'			
		self.fields['evento'].label = 'Evento pertencente'

	class Meta:
		model = Atividade		
		fields = ('nome_atividade','evento','valor_atividade','tipo_atividade','descricao')				