from .models import Emp, Account
from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'
        
class EmpForm2(forms.ModelForm):
    class Meta:
        model = Emp
        fields=['name','email','address']
        
class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'