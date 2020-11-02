from django import forms

from main.models import UserRequest


class CreateRequestForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = UserRequest
        fields = [
            'name',
            'message',
            'phone_number',
        ]
