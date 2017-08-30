from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [	

	url(r'^cadastroCupom/$',views.CadastroCupom.as_view(), name='cadastro_cupom'),

]