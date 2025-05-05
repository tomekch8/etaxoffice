from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'firstname', 'lastname', 'company_name',
            'nip', 'street', 'number_street', 'postal_code', 'city',
            'pkd_number', 'vat_payer', 'form_of_taxation',
            'password1', 'password2',
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'email', 'firstname', 'lastname', 'street', 'number_street',
            'postal_code', 'city', 'vat_payer', 'form_of_taxation'
        ]
