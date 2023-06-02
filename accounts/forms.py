from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    # add extra field
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # a function to save cleaned data from the form
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False) # super function is refering to Parent class
        user.email = self.cleaned_data["email"] # handling additional fields
        if commit:
            user.save()
        return user