from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	

	url(r'^cadastroEvento/$',views.cadastroEvento.as_view(), name='cadastro_evento'),
	url(r'^cadastroAtividade/$', views.CadastroAtividade.as_view(), name='cadastro_atividade'),
	url(r'^cadastroCupom/$',views.cadastroCupom.as_view(), name='cadastro_cupom'),

]