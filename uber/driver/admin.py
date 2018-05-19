from django.contrib import admin
from .models import Driver, DriverLocation, Car

# Register your models here.
admin.site.register(Driver)
admin.site.register(DriverLocation)
admin.site.register(Car)