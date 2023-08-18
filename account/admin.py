from django.contrib import admin

# Register your models here.
from .models import User, Profile, Address

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id',)