from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

# Form für Login
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Form für Registrierung
class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('manager', 'Restaurant Manager'),
      # ('staff', 'Staff Member'), # Staff Member derzeit ungenutzt, aber für Scalability bereits angelegt
        
        # Marketing Member Rolle muss vom Admin separat vergeben werden, um Sicherheitslücken zu vermeiden
    ]
    
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label='Role')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user
    
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username']  # Füge hier alle Felder hinzu, die der Nutzer bearbeiten können soll