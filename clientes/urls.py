from django.urls import path
from . import views

urlpatterns = [
    path('crud_clientes', views.crud_clientes, name='crud_clientes'),
    path('clientes_add', views.clientes_ag, name='clientes_add'),
    path('clientes_edit/<int:pk>', views.clientes_edit, name='clientes_edit'),
    path('clientesUpdate/<str:pk>/', views.clientesUpdate, name='clientesUpdate'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
]
