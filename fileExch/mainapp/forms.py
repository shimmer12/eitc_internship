from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "status", "photo", "approver", "history"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""



from django.contrib.auth.forms import UserCreationForm
from mainapp.models import User  # Import your custom User model

class UserRegisterForm(UserCreationForm):
    ACCESS_LEVEL_CHOICES = [
        ('Dispatch', 'Dispatch'),
        ('SectionOffice', 'Section Office'),
        ('HOD', 'Head of Department'),
    ]
    access_level = forms.ChoiceField(choices=ACCESS_LEVEL_CHOICES, required=True)
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User  # Use your custom User model
        fields = ['username', 'email', 'password1', 'password2', 'access_level']
