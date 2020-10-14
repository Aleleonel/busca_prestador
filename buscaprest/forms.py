from django import forms
from .models import Prestador


class PrestadoresForm(forms.ModelForm):

    class Meta:
        model: Prestador
        fields = 'all'