from django.forms import ModelForm
from .models import Shoe


class EditShoeForm(ModelForm):
    class Meta:
        model = Shoe
        fields = '__all__'


