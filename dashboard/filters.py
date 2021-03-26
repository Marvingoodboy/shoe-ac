import django_filters

from .models import Shoe


# Dashboard filter shoes
class ShoeFilter(django_filters.FilterSet):
    class Meta:
        model = Shoe
        fields = ['season', 'type', 'place']
