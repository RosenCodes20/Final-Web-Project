from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_filter = ['email', 'last_login']
    search_fields = ['email']
    ordering = ['-last_login']
    readonly_fields = ['password']
    list_display = ['email', 'last_login']