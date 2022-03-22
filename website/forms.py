from ctypes import resize
from dataclasses import field
from django import forms
from website.models import Contact,Newsletter

class NameForm(forms.Form):
    name = forms.CharField(label='Your Name',max_length=225)
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(label='Your Subject',max_length=300)
    message = forms.CharField(label='Your Message',widget=forms.Textarea(attrs={'cols':40,'rows':10}))
  
    
class Contactform(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
class Newsletterform(forms.ModelForm):
     class Meta:
         model = Newsletter
         fields = '__all__'