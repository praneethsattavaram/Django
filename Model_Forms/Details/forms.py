from django import forms
from .models import LaptopDetails

class LaptopDetailsForm(forms.ModelForm):
    class Meta:
        model = LaptopDetails
        fields = ['name']