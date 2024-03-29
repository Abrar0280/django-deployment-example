from django import forms
from django.core import validators
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_mail = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(selfself):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Emails donot match")
