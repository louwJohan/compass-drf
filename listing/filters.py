from django_filters import rest_framework as filters
from .models import Listing

class ListingFilter(filters.FilterSet):
    
    class Meta:
        model = Listing
        fields = {'area': ['icontains'], 'type_of_property': ['exact'],
                  'price': ['icontains'], 'bedrooms':['exact'],
                  'owner__followed__owner__profile':['exact'],
                  'saved__owner__profile':['exact'],
                  'owner__profile':['exact'],
                  'commerce_type':['exact'],
                  'owner':['exact'],}