from django.shortcuts import render, redirect
from .forms import ProfileForm

def upload_image(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ProfileForm()
    return render(request, 'upload_image.html', {'form': form})