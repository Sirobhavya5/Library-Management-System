from django import forms

class BorrowForm(forms.Form):
    email = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)

class UnborrowForm(forms.Form):
    email = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    