from django import forms

class BasicForm(forms.Form):
    name = forms.CharField(
        label='Name', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='Username', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
