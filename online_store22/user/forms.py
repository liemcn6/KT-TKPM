from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg'}
    ))

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
      attrs={'class': 'form-control form-control-lg'}
    ))
    last_name = forms.CharField(widget=forms.TextInput(
      attrs={'class': 'form-control form-control-lg'}
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg'}
    ))


