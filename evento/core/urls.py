from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	

	url(r'^cadastroEvento/$',views.CadastroEvento.as_view(), name='cadastro_evento'),
	url(r'^cadastroAtividade/$', views.CadastroAtividade.as_view(), name='cadastro_atividade'),
	url(r'^criarEquipe/$',views.CriarEquipe.as_view(), name='criar_equipe'),
	url(r'^associarEvento/$',views.AssociarEvento.as_view(), name='associar_evento'),

]