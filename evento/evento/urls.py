from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	
<<<<<<< HEAD
	url(r'^cadastroEvento/$',views.cadastro_evento, name='cadastro_evento'),
	url(r'^cadastroAtividade/$',views.cadastro_atividade, name='cadastro_atividade'),
=======
	url(r'^cadastroEvento/$',views.cadastroEvento, name='cadastro_evento'),
	url(r'^cadastroAtividade/$',views.cadastroAtividade, name='cadastro_atividade'),
	url(r'^cadastroCupom/$',views.cadastroCupom, name='cadastro_cupom'),
>>>>>>> master
]