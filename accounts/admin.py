from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "username", "email","first_name",
        "last_name", "role", "dept",
        "is_staff"
    ]
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "dept")}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "dept")}),
    )

admin.site.register(CustomUser, CustomUserAdmin) 