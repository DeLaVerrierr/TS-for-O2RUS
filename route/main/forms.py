from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Profile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, required=False, label='Current Password')
    new_password = forms.CharField(widget=forms.PasswordInput, required=False, label='New Password')

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'new_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        new_password = cleaned_data.get('new_password')

        if password and not self.instance.user.check_password(password):
            raise forms.ValidationError('Incorrect password.')

        if new_password:
            if not password:
                raise forms.ValidationError('Current password is required for changing password.')
            if password == new_password:
                raise forms.ValidationError('New password should be different from the current password.')

        return cleaned_data

