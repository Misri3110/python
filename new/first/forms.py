from django import forms

class RegisterData(forms.Form):
    Name = forms.CharField()