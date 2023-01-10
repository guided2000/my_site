from django import forms
from blog.models import Newsletter
from captcha.fields import CaptchaField

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'