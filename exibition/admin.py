from django.contrib import admin
from .models import Breed, Dog, Owner, Judge, Show, Sponsor


admin.site.register(Judge)
admin.site.register(Show)
admin.site.register(Sponsor)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    search_fields = ['name']
    prepopulated_fields = {
        'slug': ['name']
    }


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'breed', 'gender']
    autocomplete_fields = ['owner', 'breed']
    search_fields = ['breed']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
