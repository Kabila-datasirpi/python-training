
# forms.py
from django import forms
from .models import employee

class ModelForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['eid', 'ename', 'econtact']
