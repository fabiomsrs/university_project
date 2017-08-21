from django import forms
from evento.models import Evento
class FormEventoAssociado(forms.ModelForm):
	"""docstring for FormAssociarEventos"""
	def __init__(self, arg):
		self.user = kwargs.pop("user")
		super(FormAssociarEventos, self).__init__(*args, **kwargs)
		
		self.fields['evento_principal'].queryset =  self.Evento.objects.all()
		self.fields['evento_principal'].label =  'associar a evento'
			
	class Meta:
		model = Evento	
		fields = ('nome_evento','evento_principal')

class FormEventoAssocia(forms.ModelForm):
	def __init__(self, arg):
		self.user = kwargs.pop("user")
		super(FormAssociarEventos, self).__init__(*args, **kwargs)
		
		self.fields['evento_principal'].queryset =  self.Evento.objects.all()
		self.fields['evento_principal'].label =  'associar a evento'
