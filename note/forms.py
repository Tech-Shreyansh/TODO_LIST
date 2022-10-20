from django.forms import ModelForm
from .models import category,topic,description

class catform(ModelForm):
    class Meta:
        model = category
        fields = '__all__'

class noteform(ModelForm):
    class Meta:
        model = description
        fields = '__all__'

class topicform(ModelForm):
    class Meta:
        model = topic
        fields = '__all__'