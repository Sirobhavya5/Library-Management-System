from django import forms

ROLE_CHOICES =(
    ("1", "Member"),
    ("2", "Employee"),
    ("3", "Owner")
)

class UserSignUpForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"type": "password"}))
    password_confirmation = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"type": "password"}))
    role = forms.ChoiceField(choices = ROLE_CHOICES)
    street = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    zip_code = forms.CharField(max_length=255)

class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"type": "password"}))