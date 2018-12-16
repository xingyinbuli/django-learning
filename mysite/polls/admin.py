from django.contrib import admin

# Register your models here.
from polls.models import Choice
admin.site.register(Choice)