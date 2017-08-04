from django import forms
from tag.models import TagEvento,TagUsuario

class AddTagUsuario(forms.ModelForm):
	class Meta:
		model = TagUsuario
		exclude = ['usuario']
		fields = ('usuario','nome_tag')				

class AddTagEvento(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user") #recebendo usuario logado
		super(AddTagEvento, self).__init__(*args, **kwargs)		
	
		self.fields['evento'] = forms.ModelMultipleChoiceField(self.user.meus_eventos.all())
		self.fields['evento'].empty_label = 'Empty'			
		self.fields['evento'].label = 'Evento'

	class Meta:
		model = TagEvento	
		fields = ('nome_tag','evento')
		widgets={ 'evento' : forms.Select}