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


class OnlineOfferForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'contact_email', 'placeholder': 'Email'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'id': 'contact_subject', 'placeholder': 'Subject'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'id': 'contact_message', 'placeholder': 'Message', 'rows':'4'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'contact_name', 'placeholder': 'Name'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'id':'contact_subject', 'placeholder': 'Phone', 'restrict': 'A-Z\a-z\0-9'}), required=True)
