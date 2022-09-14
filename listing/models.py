from django.db import models
from django.contrib.auth.models import User

PROPERTY_TYPE = (('detached_house', 'Detached House'),
                 ('terrace_house', 'Terrace House'),
                 ('apartment', 'Apartment'),
                 ('semi_detached', 'Semi-detached'),
                 ('bungalows', 'Bungalows')
                )

COMMERCE_TYPE = (('sell', 'Sell'), ('rent', 'Rent'))

class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type_of_property = models.CharField(choices=PROPERTY_TYPE, max_length=15)
    bedrooms = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    commerce_type = models.CharField(choices=COMMERCE_TYPE, max_length=15)
    image_one = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    image_two = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    image_three = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    image_four = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    image_five = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    image_six = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    image_seven = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    image_eight = models.ImageField(upload_to='images/', default='../Placeholder-Clipart-Icon_dhzywt.png')
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}' 
