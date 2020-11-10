from django.shortcuts import render
from .forms import ImageModelForm
from .models import ImageModel

# Create your views here.

def index_view(request):
    if request.method == "POST":
        form = ImageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageModelForm()
    img = ImageModel.objects.all()      
    return render(request,'imgapp/index.html',{'form':form,'img':img})