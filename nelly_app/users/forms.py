from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms


UserModel = get_user_model()


class CreateProfileForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {
            'username': UsernameField
        }
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'password1'})
        }

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)

        super().__init__(*args, **kwargs)
        for field_name in ['password1', 'password2']:
            self.fields[field_name].help_text = None

