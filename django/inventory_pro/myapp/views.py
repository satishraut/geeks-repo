from django.shortcuts import render, redirect, get_object_or_404
from .models import (Laptop, Mobile, Desktop)
from .forms import (LaptopForm,DesktopForm,MobileForm)
# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

def displya_laptop(request):
    items = Laptop.objects.all()
    return render(request,'myapp/index.html',{'items':items,"device":"Laptops"})

def display_mobile(request):
    items = Mobile.objects.all()
    return render(request,'myapp/index.html',{'items':items,"device":"Mobiles"})

def display_desktop(request):
    items = Desktop.objects.all()
    return render(request,'myapp/index.html',{'items':items,"device":"Desktop"})

def add_device(request, cls):
    if request.method == "POST":
         print("Ture")
         form = cls(request.POST)
         if form.is_valid():
            form.save()
         return redirect("index")
    else:
        form = cls()
    
    return render(request,'myapp/add_laptop.html',{'form':form})

def add_laptop(request):
    return add_device(request, LaptopForm)

def add_mobile(request):
    return add_device(request, MobileForm)

def add_desktop(request):
    return add_device(request, DesktopForm)

def edit_device(request,pk, model, cls):
     item = get_object_or_404(model, pk=pk)
     if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
     else:
        form = cls(instance=item)

        return render(request, 'myapp/edit_item.html', {'form': form})

def edit_laptop(request,pk):
    return edit_device(request,pk,Laptop,LaptopForm)

def edit_mobile(request,pk):
    return edit_device(request,pk,Mobile,MobileForm)

def edit_desktop(request,pk):
    return edit_device(request,pk,Desktop,DesktopForm)

def delete_device(request,pk, model):
    print(pk,model)
    model.objects.filter(pk=pk).delete()
    items = model.objects.all()
    return render(request,'myapp/index.html',{'items':items})

def delete_laptop(request,pk):
    return delete_device(request,pk, Laptop)

def delete_mobile(request,pk):
    return delete_device(request,pk, Mobile)

def delete_desktop(request,pk):
    return delete_device(request,pk, Desktop)





