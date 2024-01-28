#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('crud_boletas', views.crud_boletas, name='crud_boletas'),
    path('boletas_add', views.boletas_ag, name='boletas_add'),
    path('boletas_edit/<str:pk>', views.boletas_edit, name='boletas_edit'),
    path('boletasUpdate', views.boletasUpdate, name='boletasUpdate'),
    path('boletas_del/<str:pk>', views.boletas_del, name='boletas_del'),
]