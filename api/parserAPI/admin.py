from django.contrib import admin
from .models import Ticket, File, AdditionalFields
from .models import File
# Register your models here.
admin.site.register(File)
admin.site.register(Ticket)
admin.site.register(AdditionalFields)