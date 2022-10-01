from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return self.listing.title
