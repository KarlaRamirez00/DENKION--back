#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('crud_boletas', views.crud_boletas, name='crud_boletas'),
    path('boletas_add', views.boletas_ag, name='boletas_add'),
    path('boletas_edit/<int:pk>/', views.boletas_edit, name='boletas_edit'),
    path('boletasUpdate/<int:pk>/', views.boletasUpdate, name='boletasUpdate'),  # Añade el patrón con un parámetro de variable 'pk'
    path('boletas_del/<str:pk>', views.boletas_del, name='boletas_del'),
]



