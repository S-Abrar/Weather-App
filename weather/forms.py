# weather/forms.py
from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter city name',
        'id': 'city-input',
        'autocomplete': 'off'
    }))
