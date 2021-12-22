from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from WebTraining.web_training_auth.models import WebTrainingUser
UserModel = get_user_model()

@admin.register(UserModel)
class WebTrainingUserAdmin(UserAdmin):
    list_display = ['email','is_staff']
    list_filter = ['is_staff','is_superuser','groups']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (( 'Permissions' ), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (( 'Important dates' ), {'fields': ('last_login', )}),
    )