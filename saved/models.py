from django.db import models
from django.contrib.auth.models import User
from listing.models import Listing

class Saved(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'listing']

    def __str__(self):
        return f'{self.owner} , {self.listing}'
