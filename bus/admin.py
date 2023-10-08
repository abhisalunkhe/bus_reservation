from django.contrib import admin
from .models import Bus, Reservation

# Register your models here.

class admin_bus(admin.ModelAdmin):
    list_display = ['id', 'name', 'route', 'distance', 'bus_type', 'available_seats']

class admin_reservation(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone', 'adults', 'childrens', 'total_fare', 'bus_name', 'route', 'bus_type', 'duration']

admin.site.register(Bus, admin_bus)
admin.site.register(Reservation, admin_reservation)