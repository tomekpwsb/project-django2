from django import forms

class MyForm(forms.Form):
    my_field = forms.CharField(label='Input your name:')