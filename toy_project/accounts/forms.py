from django import forms
from django.db.models import fields
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname', 'phone_number', 'gender')
