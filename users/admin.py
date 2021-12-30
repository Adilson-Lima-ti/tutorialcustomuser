from django.contrib import admin
from django.contrib.auth import admin as auth_admin # essa importação faz aparecer os campos corretamente em admin
from .forms import UserCreationForm, UserChangeForm

from .models import User # criada digitando código




@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("cliente", )}),
    )
