from django.contrib import admin
from .models import Ticket, File
from .models import File
from .models import FinalTicket
# Register your models here.
admin.site.register(File)
admin.site.register(Ticket)
admin.site.register(FinalTicket)
