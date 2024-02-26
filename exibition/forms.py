from django import forms
from .models import Breed, Dog, Owner, Judge, Show, Sponsor


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name',
                  'email', 'phone', 'address', 'user']
