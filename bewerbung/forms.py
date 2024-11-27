from django import forms
from .models import Bewerbung

class BewerbungForm(forms.ModelForm):
    class Meta:
        model = Bewerbung
        fields = ['name', 'company', 'position', 'date_applied', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'date_applied': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
