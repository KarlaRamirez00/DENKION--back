#from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('crud_clientes', views.crud_clientes, name='crud_clientes'),
    path('clientes_add', views.clientes_ag, name='clientes_add'),
    path('clientes_edit/<str:pk>', views.clientes_edit, name='clientes_edit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
]
