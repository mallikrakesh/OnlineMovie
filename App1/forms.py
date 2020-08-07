from App1.models import *
from django import forms

class MovieAdminForm(forms.ModelForm):
    class Meta:
        model=MovieAdmin
        fields='__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model=LoginModel
        fields='__all__'