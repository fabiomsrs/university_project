from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	
	url(r'^cadastroEvento/$',views.cadastroEvento, name='cadastro_evento'),
	url(r'^cadastroAtividade/$',views.cadastroAtividade, name='cadastro_atividade'),
]