from django import forms
from django.conf import settings

from .models import Accounting


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = ['first_name', 'last_name', 'date_of_birth', 'finances', ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'finances': forms.FileInput(attrs={'accept': '.xlsx, .xls, '})
        }
