from django.contrib import admin

# Register your models here.

# apps/your_app/admin.py

from django.contrib import admin
from .models import Category, MenuItem, About, Booking


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')  # Adjust fields as needed
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')  # Adjust fields as needed
    search_fields = ('title',)


@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'phone_number', 'booking_date')

#
# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone_number', 'email', 'booking_date')
#     search_fields = ('name', 'email')
#     list_filter = ('booking_date',)
