import json
from django import forms
from evento.models import Evento, Atividade
from inscricao.models import Inscricao

class InscricaoForm(forms.ModelForm):
	lista_atividade = {}
	lista_eventos = []	

	for atividade in Atividade.objects.all():
		if atividade.evento.nome_evento in lista_atividade:
			lista_atividade[atividade.evento.nome_evento].append(atividade.nome_atividade)
		else:
			lista_atividade[atividade.evento.nome_evento] = [atividade.nome_atividade]
		lista_eventos.append((atividade.nome_atividade,atividade.nome_atividade))

	eventos = [str(evento) for evento in Evento.objects.all()]

	evento = forms.ChoiceField(choices=([(evento, evento) for evento in eventos]))
	atividade = forms.ChoiceField(choices=(lista_eventos))

	eventos = json.dumps(eventos)
	atividades_por_evento = json.dumps(lista_atividade)

	class Meta:
		model = Inscricao		
		fields = ('evento','atividade')		