from django import forms
from core.models import Atividade, Responsavel

class AtividadeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user")
		super(AtividadeForm, self).__init__(*args, **kwargs)		
	
		self.fields['evento'].queryset =  self.user.meus_eventos.all()
		self.fields['evento'].empty_label = 'Empty'			
		self.fields['evento'].label = 'Evento pertencente'

	class Meta:
		model = Atividade
		exclude = ['usuario_criador','responsavel','horario_inicio','horario_final','atividades_proibidas','local']		
		fields = '__all__'


class ResponsavelForm(forms.ModelForm):	
	class Meta:
		model = Responsavel		
		fields = '__all__'		