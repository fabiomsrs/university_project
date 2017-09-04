from django import forms
from core.models import Atividade, Responsavel

class AtividadeForm(forms.ModelForm):		

	class Meta:
		model = Atividade
		exclude = ['usuario_criador', 'horario_inicio','horario_final','atividades_proibidas','local','evento','responsavel']		
		fields = '__all__'


class ResponsavelForm(forms.ModelForm):	
	class Meta:
		model = Responsavel		
		fields = '__all__'		