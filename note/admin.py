from django.contrib import admin

# Register your models here.
from .models import category,topic,description

admin.site.register(category)
admin.site.register(topic)
admin.site.register(description)