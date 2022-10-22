from rest_framework import serializers
from .models import description

class descriptionS(serializers.Serializer):
    topic = serializers.CharField(max_length=2000)
    description = serializers.CharField(max_length=2000)
    time = serializers.DateTimeField()
    time_updated = serializers.DateTimeField()

    # def create(self, validate_data):
    #     return description.objects.create(**validate_data)

# class descriptionform(forms.Form):
#     topic = forms.CharField(max_length=2000)
#     description = forms.CharField(max_length=2000)
#     time = forms.DateTimeField()
#     time_updated = forms.DateTimeField()
#     bookmark = forms.IntegerField()
