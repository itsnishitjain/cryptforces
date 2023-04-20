from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from cryptforces.forms import CustomUserChangeForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'points',) # Add your custom field to the list_display
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name','last_name', 'email')}), # Add your custom field to the 'Personal Info' section
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Stats', {'fields': ('points',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
