# forms.py
from django import forms

class InvestmentForm(forms.Form):
    amount = forms.DecimalField(label='Investment Amount', min_value=1000)
