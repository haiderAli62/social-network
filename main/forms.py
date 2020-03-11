from django import forms
from .models import User , Post
from django.core.exceptions import ValidationError

CHOICES = [('ceo', 'ceo'),
           ('hr', 'hr'),
           ('cto', 'cto'),
           ('sse', 'senior software engineer'),
           ('jse', 'junior software engineer'), ]


class UploadPostForm(forms.Form):
    title = forms.CharField(max_length=250)
    description = description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post



class SignupFormCeo(forms.Form):

    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    #choise = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):

        user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1'],
                is_ceo=True
        )
        return user


class SignupFormHr(SignupFormCeo):

    def save(self, commit=True):
        user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1'],
                is_hr=True
        )
        return user

class SignupFormCto(SignupFormCeo):

    def save(self, commit=True):
        user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1'],
                is_cto=True
        )
        return user


class SignupFormSeniorSE(SignupFormCeo):

    def save(self, commit=True):
        user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1'],
                is_senior_developer=True
        )
        return user



class SignupFormJuniorSE(SignupFormCeo):

    def save(self, commit=True):
        user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1'],
                is_junior_developer=True
        )
        return user