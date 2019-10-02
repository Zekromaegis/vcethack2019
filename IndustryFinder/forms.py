from django.contrib.auth.models import User
#from django.utils.translation import gettext_lazy as _
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password'] 