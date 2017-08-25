from django import forms
from evento.models import Atividade, Responsavel

class AtividadeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user")
		super(AtividadeForm, self).__init__(*args, **kwargs)		
	
		self.fields['evento'].queryset =  self.user.meus_eventos.all()
		self.fields['evento'].empty_label = 'Empty'			
		self.fields['evento'].label = 'Evento pertencente'

	class Meta:
		model = Atividade
		exclude = ['usuario_criador','responsavel','data_inicio','data_de_fim','hora_inicio','hora_fim','atividades_proibidas']		
		fields = '__all__'


class ResponsavelForm(forms.ModelForm):	
	class Meta:
		model = Responsavel		
		fields = '__all__'		