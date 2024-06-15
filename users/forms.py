from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Form für Login
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Form für Registrierung
class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('restaurant_manager', 'Restaurant Manager'),
    ]
    
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label='Role')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user