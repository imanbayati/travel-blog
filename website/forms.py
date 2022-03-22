from ctypes import resize
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your Name',max_length=225)
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(label='Your Subject',max_length=300)
    message = forms.CharField(label='Your Message',widget=forms.Textarea(attrs={'cols':40,'rows':10}))