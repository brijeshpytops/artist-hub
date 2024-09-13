from django.contrib import admin
from .models import Artist, ArtistProfile
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['artist_id', 'email', 'mobile']
    search_fields = ['artist_id', 'email', 'mobile']
admin.site.register(Artist, ArtistAdmin)

class ArtistProfileAdmin(admin.ModelAdmin):
    list_display = ['artist_id_id', 'first_name', 'last_name', 'gender', 'date_of_birth']
    list_filter = ['gender']
    list_per_page = 10
admin.site.register(ArtistProfile, ArtistProfileAdmin)