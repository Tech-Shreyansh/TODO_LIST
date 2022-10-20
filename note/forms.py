from django.forms import ModelForm
from .models import category

class catform(ModelForm):
    class Meta:
        model = category
        fields = '__all__'