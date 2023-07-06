from django.contrib import admin
from .models import parseInput
from .models import File
# Register your models here.
admin.site.register(parseInput)
admin.site.register(File)