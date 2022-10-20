from django.contrib import admin

# Register your models here.
from .models import trial,trial_class,trial_skill

admin.site.register(trial)
admin.site.register(trial_class)
admin.site.register(trial_skill)