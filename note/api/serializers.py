from dataclasses import field
from rest_framework.serializers import ModelSerializer
from note.models import *

class NotesSerializer(ModelSerializer):
    class Meta:
        model = description
        fields = '__all__'

class TopicSerializer(ModelSerializer):
    class Meta:
        model = topic
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

    # def create(self, validate_data):
    #     return description.objects.create(**validate_data)

# class descriptionform(forms.Form):
#     topic = forms.CharField(max_length=2000)
#     description = forms.CharField(max_length=2000)
#     time = forms.DateTimeField()
#     time_updated = forms.DateTimeField()
#     bookmark = forms.IntegerField()
