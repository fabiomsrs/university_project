from django import forms
from comum.models import TagEvento,TagUsuario

class AddTagUsuario(forms.ModelForm):
	class Meta:
		model = TagUsuario
		exclude = ['usuario']
		fields = ('usuario','nome_tag')				

class AddTagEvento(forms.ModelForm):
	class Meta:
		model = TagEvento
		exclude = ['evento']			
		fields = '__all__'		