from django.forms import ModelForm
from django.http import request

from .models import Shoe

class EditShoeForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ('place', 'size', 'quantity', 'type',
                  'season', 'model', 'male', 'image')


class CreateShoeForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ('place', 'size', 'quantity', 'type',
                  'season', 'model', 'male', 'image')
