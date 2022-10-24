from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)
