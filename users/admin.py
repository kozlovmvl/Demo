from django.contrib import admin

from .models import City, Country, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "id"]
    autocomplete_fields = ["country", "city"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    search_fields = ["name"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    search_fields = ["name"]
