from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import MyUser


class RegistrationForm(ModelForm):
    username = forms.CharField( label=(u'User name'))
    username.widget.attrs.update( {'type' : "login", 'class':"form-control", 'placeholder':"username"})
    email = forms.EmailField( label=(u'Email Address'),)
    email.widget.attrs.update( {'type' : "email", 'class':"form-control", 'placeholder':"email"})
    first_name = forms.CharField( label=(u'Nickname'),)
    first_name.widget.attrs.update( {'type' : "NickName", 'class':"form-control",  'placeholder':"first_name"})
    password = forms.CharField( label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password.widget.attrs.update( {'type' : "Password", 'class':"form-control",  'placeholder':"password"})
    repeatedPassword = forms.CharField( label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    repeatedPassword.widget.attrs.update( {'type' : "Retype password", 'class':"form-control", 'placeholder':"Repeated password"})

    class Meta:
        model = MyUser
        exclude = ('user',)


def clean_username(self):
    username = self.cleaned_data['username']
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return username
    raise  forms.ValidationError("Username is already taken")
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The passwords did not match.  Please try again.")
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField( label=(u'User name'))
    username.widget.attrs.update( {'type' : "login", 'class':"form-control", 'placeholder':"Login"})
    password = forms.CharField( label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password.widget.attrs.update( {'type' : "Password", 'class':"form-control",  'placeholder':"Password"})
    class Meta:
        model = MyUser
        exclude = ('user',)