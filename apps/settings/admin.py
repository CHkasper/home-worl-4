from django.contrib import admin
from apps.settings.models import Settings, Text, Image
# Register your models here.
admin.site.register(Settings)
admin.site.register(Text)
admin.site.register(Image)