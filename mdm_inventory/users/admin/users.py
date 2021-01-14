# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# models
from mdm_inventory.users.models import User


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User
    list_display = ('id', 'email', 'is_verified', 'is_staff',)
    list_filter = ('is_verified','is_manager','is_cashier', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'profile_picture', 'is_active')}),
        ('Permissions', {'fields': ('is_verified', 'is_staff', 'is_superuser','is_manager','is_cashier',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_verified', 'is_staff', 'is_superuser', 'profile_picture','is_manager','is_cashier',)
        }),
    )
    search_fields = ('email', 'username',)
    # # I overwrite the save_model method for creating and sending mail

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)

    # def delete_queryset(self, request, queryset):

admin.site.register(User, CustomUserAdmin)