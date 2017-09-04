from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	
	url(r'^tagUsuario/$',views.adicionarTagUsuario.as_view(), name='tag_usuario'),
	url(r'^(?P<pk>\d+)/tagEvento/$',views.adicionarTagEvento.as_view(), name='tag_evento'),
]