from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	

	url(r'^cadastroEvento/$',views.cadastro_evento, name='cadastro_evento'),
	url(r'^cadastroAtividade/$',views.cadastro_atividade, name='cadastro_atividade'),
	url(r'^cadastroCupom/$',views.cadastro_cupom, name='cadastro_cupom'),

]