from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'fullname', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Zusätzliche Felder', {'fields': ('fullname',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Zusätzliche Felder', {'fields': ('fullname',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
