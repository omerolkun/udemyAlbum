from django import forms
from .models import Musician

class user_form(forms.Form):
    user_name = forms.CharField()
    user_email = forms.EmailField()

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        
        fields = '__all__'