from django import forms
from .models import Producto
from .models import Cliente
from .models import Boleta

class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = ['fecha', 'cliente', 'producto', 'total', 'metodo_pago', 'estado']

    def __init__(self, *args, **kwargs):
        super(BoletaForm, self).__init__(*args, **kwargs)

        # Campo de fecha con formato legible
        self.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

        # Campo de cliente como un Select con nombres y apellidos concatenados
        self.fields['cliente'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['cliente'].label_from_instance = lambda obj: f"{obj.nombre} {obj.apellido_paterno}"

        # Campo de producto como un Select con todos los productos
        self.fields['producto'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['producto'].queryset = Producto.objects.all()

