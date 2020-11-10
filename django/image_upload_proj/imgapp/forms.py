from django.forms import ModelForm
from .models import ImageModel


class ImageModelForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = "__all__"
        lables = {'photo':''}
