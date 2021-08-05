from django import forms
from django.db.models.fields import DateField
from django.forms import fields
from .models import Album, Musician

class user_form(forms.Form):
    user_name = forms.CharField()
    user_email = forms.EmailField()

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    rel_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Album
        fields='__all__'