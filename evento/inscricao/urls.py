from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^cadastrarInscricao/$',views.Inscricao.as_view(), name='inscricao'),
	url(r'^(?P<pk>\d+)/cadastroCupom/$',views.CadastroCupom.as_view(), name='cadastro_cupom'),	
]
