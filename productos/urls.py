#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('crud_productos', views.crud_productos, name='crud_productos'),
    path('productos_add', views.productos_ag, name='productos_add'),
    path('productos_edit/<str:pk>', views.productos_edit, name='productos_edit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
]