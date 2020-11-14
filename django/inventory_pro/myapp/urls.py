from django.urls import path
from .views import (index, displya_laptop, display_mobile,display_desktop,add_laptop,
                    add_mobile,add_desktop, edit_laptop, edit_mobile, edit_desktop,
                    delete_laptop,delete_mobile,delete_desktop)
urlpatterns = [
    path('', index, name='index'),
    path('display-laptop', displya_laptop, name='displya-laptop'),
    path('display-desktop', display_desktop, name='displya-desktop'),
    path('display-mobile', display_mobile, name='displya-mobile'),

    path('add-laptop', add_laptop, name='add-laptop'),
    path('add-mobile', add_mobile, name='add-mobile'),
    path('add-desktop', add_desktop, name='add-desktop'),

    path('edit-laptop/<int:pk>', edit_laptop, name='edit-laptop'),
    path('edit-mobile/<int:pk>', edit_mobile, name='edit-mobile'),
    path('edit-desktop/<int:pk>', edit_desktop, name='edit-desktop'),

    path('delete-laptop/<int:pk>', delete_laptop, name='delete-laptop'),
    path('delete-mobile/<int:pk>', delete_mobile, name='delete-mobile'),
    path('delete-desktop/<int:pk>', delete_desktop, name='delete-desktop'),

]
