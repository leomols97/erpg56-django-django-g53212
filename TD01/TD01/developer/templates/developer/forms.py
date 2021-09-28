from django import forms

from developer.models import Developer


class DeveloperForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(max_length=100)
