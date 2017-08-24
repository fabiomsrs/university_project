from django import forms
from evento.models import Evento
from django.contrib.auth.models import User

class FormEventoPrincipal(forms.ModelForm):	
	def __init__(self, *args, **kwargs):
		self.eventos = kwargs.pop("eventos")
		super(FormEventoPrincipal, self).__init__(*args, **kwargs)	
		self.fields['evento_satelite'] = forms.ChoiceField(choices=([(evento, evento) for evento in self.eventos]))
			
	class Meta:
		model = Evento	
		fields = ['evento_principal']

	
