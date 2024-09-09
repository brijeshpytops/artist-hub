from django.db import models
from django.contrib.auth.hashers import make_password
from cryptography.fernet import Fernet

from AHApps.master.models import TimestampModel
from AHApps.master.utils.UNIQUE.generate_password import create_password
from AHApps.master.utils.EMAILS.login_credential import send_welcome_email

# Create your models here.
class Artist(TimestampModel):
    artist_id = models.CharField(primary_key=True, max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    mobile = models.CharField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if not self.artist_id:
            last_artist_id = Artist.objects.all().order_by('-created_at').first()
            if last_artist_id:
                new_artist_id = "AH000" + str(int(str(last_artist_id.artist_id)[5:]) + 1)
            else:
                new_artist_id = "AH0001"

            self.artist_id = new_artist_id

        if not self.password:
            self.password = make_password(create_password())

        if self.is_active:
            send_welcome_email(self.artist_id, self.email, )
            self.is_active = False


        super(Artist, self).save(*args, **kwargs)