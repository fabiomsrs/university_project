from django import forms
from ..models import Usuario #Mudar Import

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('nomeUsuario','login','password')