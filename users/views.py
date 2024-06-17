# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomerProfile
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

@login_required
def profile_view(request):
    user = request.user
    customer_profile = CustomerProfile.objects.filter(user=user).first()
    context = {
        'user': user,
        'customer_profile': customer_profile,
    }
    return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    customer_profile = CustomerProfile.objects.filter(user=user).first()

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=customer_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('success')
    else:
        form = CustomUserChangeForm(instance=customer_profile)
    
    context = {
        'user': user,
        'customer_profile': customer_profile,
        'form': form,
    }
    return render(request, 'users/success.html', context)

def success(request):
    return render(request, 'users/success.html')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    