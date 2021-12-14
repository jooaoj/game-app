from django.contrib import admin
from django.contrib.admin.decorators import register

# Registering Models to admin-site

from .models import Entry, Title

admin.site.register(Title)
admin.site.register(Entry)
