from django import forms
from .models import Pasajero

class PasajeroFormulario(forms.ModelForm):
	class Meta:
		model = Pasajero
		fields = '__all__'