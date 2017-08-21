from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^cadastrarInscricao/$',views.Inscricao.as_view(), name='inscricao')	
]
