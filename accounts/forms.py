from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm): 
    class Metal(UserCreationForm): 
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'role', 'department', 'years'
        )

class CustomUserChangeForm(UserChangeForm): 
    class Meta(UserChangeForm): 
        model = CustomUser
        fields = UserChangeForm.Meta.fields