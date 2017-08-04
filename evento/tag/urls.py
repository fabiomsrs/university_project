from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	
	url(r'^tagUsuario/$',views.adicionar_tag_usuario, name='tag_usuario'),
	url(r'^tagEvento/$',views.adicionar_tag_evento, name='tag_evento'),
]