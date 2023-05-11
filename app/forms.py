from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Home


class RentalForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['picture', 'rental_period', 'price', 'taking_time', 'sqft', 'name', 'place', 'owner', 'upload_time']
        widgets = {
            'picture': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NameForm(forms.Form):
    name = forms.CharField(label='Name')

