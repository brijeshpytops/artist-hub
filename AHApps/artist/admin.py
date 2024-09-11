from django.contrib import admin
from .models import Artist, ArtistProfile
# Register your models here.

admin.site.register(Artist)
admin.site.register(ArtistProfile)