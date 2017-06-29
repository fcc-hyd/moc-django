from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(max_length=30, required=True, label="Username")
    password = forms.CharField(max_length=30, required=True, label="Password")
    user.widget = forms.TextInput(attrs={"class": "form-control", "name": "username", "id": "username"})
    password.widget = forms.PasswordInput(attrs={"class": "form-control", "name": "password", "id": "password"})


class RegisterationForm(forms.Form):
    user = forms.CharField(max_length=30, required=True, label="Username")
    password = forms.CharField(max_length=30, required=True, label="Password")
    email = forms.EmailField(required=True, label="Email ID")
    user.widget = forms.TextInput(attrs={"class": "form-control", "name": "username", "id": "username"})
    password.widget = forms.PasswordInput(attrs={"class": "form-control", "name": "password", "id": "password"})
    email.widget = forms.EmailInput(attrs={"class": "form-control", "name": "email", "id": "email"})


class PasswordReset(forms.Form):
    email = forms.EmailField(required=True, label="Email ID")
    email.widget = forms.EmailInput(attrs={"class": "form-control", "name": "email", "id": "email"})


class Comment(forms.Form):
    comment = forms.CharField(required=True, max_length=200)
    comment.widget = forms.TextInput(attrs={"class": "form-control", "name": "comment", "placeholder":"Enter your comment"})
