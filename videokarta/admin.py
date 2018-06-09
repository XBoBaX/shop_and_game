from django.contrib import admin
from .models import Videocard, Price, Connection

admin.site.register(Connection)
admin.site.register(Videocard)
admin.site.register(Price)
