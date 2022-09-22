from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from listing.models import Listing


class Message(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='sender'
                              )
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, default="name")
    surname = models.CharField(max_length=255, default="surname")
    email = models.EmailField(max_length=254, default="mail@email.com")
    phone_number = PhoneNumberField(blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.owner}, {self.title}"
