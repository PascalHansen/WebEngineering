# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import permission_required
from .forms import CustomUserChangeForm
from django.contrib.auth.views import LogoutView

# Login View
class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'
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
    return render(request, 'users/register.html', {'form': form})

@permission_required('edit_profile', raise_exception=True)
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'users/profile.html', {'form': form})

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)