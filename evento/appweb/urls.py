from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$',views.index, name='login'),
	url(r'^cadastroUsuario/$',views.cadastroUsuario, name='cadastroUsuario'),
]
