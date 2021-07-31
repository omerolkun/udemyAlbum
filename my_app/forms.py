from django import forms

class user_form(forms.Form):
    user_name = forms.CharField()
    user_email = forms.EmailField()