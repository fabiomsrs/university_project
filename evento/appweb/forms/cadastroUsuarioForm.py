from django import forms
from usuario.models import Usuario

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('nome_usuario','login','password')