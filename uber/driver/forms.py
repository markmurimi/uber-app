from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):
    '''Update driver form'''
    class Meta:
        model = Driver
        fields = ['profile_pic', 'name', 'user', 'driverLocation', 'car', 'national_id']