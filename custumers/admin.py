from django.contrib import admin
from .models import Custumer

class CustumerAdmin(admin.ModelAdmin):

    list_display = ('id', 'age', 'name', 'email', 'passw')
    list_display_links = ('id', 'age', 'name', 'email')

admin.site.register(Custumer, CustumerAdmin)


