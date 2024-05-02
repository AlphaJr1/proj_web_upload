from django.shortcuts import render, redirect
from .forms import PhotoForm

# Create your views here.

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = PhotoForm()
    return render (request, 'menu_upload/upload_photo.html', {'form' : form})

def upload_success(request):
    return render(request, 'menu_upload/upload_success.html')

from .models import Photo
def photo_list(request):
    photos = Photo.objects.all()
    context = {'photos' : photos}
    return render(request, 'menu_upload/photo_list.html', context)