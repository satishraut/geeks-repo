from django.shortcuts import render
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Post

my_signal = Signal(providing_args=['name'])

def home_page(request):
    my_signal.send(sender=Post, name='Satish')
    return render(request, 'signal_app/index.html')

@receiver(request_finished)
def func(sender, **kwargs):
    print('Get Request completed')

@receiver(my_signal)
def func2(sender, **kwargs):
    print("\n",kwargs)

