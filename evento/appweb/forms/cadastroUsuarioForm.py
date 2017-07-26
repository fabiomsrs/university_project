from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = User		
		fields = ('first_name','username','password')