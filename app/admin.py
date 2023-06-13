from django.contrib import admin
from django.contrib import admin
from .models import Home, Happys, Cities, Agent, Blog


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'picture', 'rental_period', 'price', 'taking_time', 'sqft', 'name', 'place', 'owner', 'upload_time')


admin.site.register(Home, HomeAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'picture', 'name', 'jobs')


admin.site.register(Happys, HomeAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'picture', 'place', 'properties')


admin.site.register(Cities, HomeAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'picture', 'name', 'listing', 'properties')


admin.site.register(Agent, HomeAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'picture', 'date', 'name', 'reason')


admin.site.register(Blog, HomeAdmin)
