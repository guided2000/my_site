from django import forms
from website.models import contact
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email =forms.EmailField()
    subject =forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    


class ContactForm (forms.ModelForm):
    class Meta:
        model =contact
        fields = '__all__'    