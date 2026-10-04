from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('tipo',)}),
    )
    list_display = ['username', 'email', 'tipo', 'is_staff']


admin.site.register(Usuario, UsuarioAdmin)