from django import forms

from developer.models import Developer


class DeveloperForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(max_length=100)


class DeveloperForm(forms.ModelForm):  # forms.ModelForm plutôt que forms.Form
    # first_name = forms.CharField(label="First name", max_length=100) <- old
    # last_name = forms.CharField(label='Last name', max_length=100) <-old
    class Meta:  # <- news
        model = Developer  # <- new
        fields = ['first_name', 'last_name']  # <- new
