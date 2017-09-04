from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	

	url(r'^cadastro_evento/$',views.CadastroEvento.as_view(), name='cadastro_evento'),
	url(r'^(?P<pk>\d+)/cadastro_atividade/$', views.CadastroAtividade.as_view(), name='cadastro_atividade'),
	url(r'^meus_eventos/$',views.MeusEventos.as_view(), name='lista_eventos'),
	url(r'^eventos/$',views.Inscrever.as_view(), name='lista_outros_eventos'),
	url(r'^(?P<pk>\d+)/$',views.EventoEspecifico.as_view(), name='evento'),
	url(r'^criar_equipe/$',views.CriarEquipe.as_view(), name='criar_equipe'),
	url(r'^(?P<pk>\d+)/associar_evento/$',views.AssociarEvento.as_view(), name='associar_evento'),

]