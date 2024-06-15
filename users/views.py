# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm, CustomLoginForm

# Login View
class CustomLoginView(auth_views.LoginView):
    template_name = 'templates/login.html'
    authentication_form = CustomLoginForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'templates/register.html', {'form': form})