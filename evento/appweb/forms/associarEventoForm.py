from django import forms
from evento.models import Evento
from django.contrib.auth.models import User

class FormEventoPrincipal(forms.ModelForm):
	eventos = Evento.objects.all()
	evento_satelite = forms.ChoiceField(choices=([(evento, evento) for evento in eventos]))
	
			
	class Meta:
		model = Evento	
		fields = ['evento_principal']

	
