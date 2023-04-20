from django.contrib.auth.forms import UserChangeForm
from cryptforces.models import CustomUser

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'points',) # Add your custom field to the fields list
