
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field_name in ['username','email','password1','password2','first_name']:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update({'class':'form-control'})
