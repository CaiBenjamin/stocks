from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class StockForm(forms.Form):
    ticker = forms.CharField(label="GME TO THE MOON", max_length=4)


# This is a form