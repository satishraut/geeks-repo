from django.contrib import admin
from .models import ImageModel

# Register your models here.
@admin.register(ImageModel)
class ImgAdmin(admin.ModelAdmin):
    list_display = ['id','photo','created']
    

