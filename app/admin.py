from django.contrib import admin
from django.contrib import admin
from .models import Home


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'picture', 'rental_period', 'price', 'taking_time', 'sqft', 'name', 'place', 'owner','upload_time')


admin.site.register(Home, HomeAdmin)