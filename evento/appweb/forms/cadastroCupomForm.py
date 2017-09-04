from django import forms
from inscricao.models import Cupom

class CupomForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop("user") #recebendo usuario logado
		super(CupomForm, self).__init__(*args, **kwargs)			
		self.fields['desconto'].label = 'Desconto em porcento'

	class Meta:
		model = Cupom
		exclude = ['data_de_fim','data_de_inicio','evento']		
		fields = '__all__'	