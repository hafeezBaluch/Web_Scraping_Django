from django import forms

class UploadUrl(forms.Form):
    url = forms.URLField()