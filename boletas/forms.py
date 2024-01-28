from django import forms
from django.forms import ModelForm
from .models import Boleta

class BoletaForm(ModelForm):
    class Meta:

        model = Boleta
        fields = "__all__"