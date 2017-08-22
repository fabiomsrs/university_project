from django import forms
from django.contrib.auth.models import User
from evento.models import Evento





class EquipeForm(forms.ModelForm):
	def __init__(self, arg):
		self.user = kwargs.pop("user")
		super(EquipeForm, self).__init__(*args, **kwargs)

		self.fields['equipe'].queryset = auth.USER.objects.filter(first_name != self.user)
		self.fields['nome_evento'].queryset = self.Evento.objects.all()


	class Meta:
		model = Evento
		fields = ('equipe','nome_evento')




