from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (Laptop, Mobile, Desktop)

# @admin.register(Laptop)
# class LaptopAdmin(admin.ModelAdmin):
#     list_display = ['id','type','price','status','issue']

# @admin.register(Mobile)
# class MobileAdmin(admin.ModelAdmin):
#         list_display = ['id','type','price','status','issue']


# @admin.register(Desktop)
# class DesktopAdmin(admin.ModelAdmin):
#         list_display = ['id','type','price','status','issue']
    
@admin.register(Laptop,Mobile,Desktop)
class ImpExp(ImportExportModelAdmin):
    pass

