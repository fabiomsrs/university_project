from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$',views.index, name='login'),
	url(r'^home/$',views.home, name='home'),	
	url(r'^cadastroUsuario/$',views.cadastroUsuario, name='cadastro_usuario'),
	url(r'^cadastroEvento/$',views.cadastroEvento, name='cadastro_evento'),
	url(r'^cadastroAtividade/$',views.cadastroAtividade, name='cadastro_atividade'),
	url(r'^$',views.logout, name='logout'),
]
