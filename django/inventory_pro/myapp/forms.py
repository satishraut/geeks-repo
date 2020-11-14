from django.forms import ModelForm
from .models import (Laptop, Desktop, Mobile)

class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ('type','price','status','issue')

class DesktopForm(ModelForm):
    class Meta:
        model = Desktop
        fields = ('type','price','status','issue')

class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = ('type','price','status','issue')
