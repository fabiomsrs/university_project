from django.contrib.auth import User

class EquipeForm(forms.ModelForm):
	def __init__(self, arg):
		self.user = kwargs.pop("user")
		super(EquipeForm, self).__init__(*args, **kwargs)

		self.fields['membros'].queryset = User.objects.
		self.fields['Evento'].queryset = self.Evento.objects.all()


	class Meta:
		model = Evento
		fields = ('membros','Evento')
