from django.contrib import admin
from .models import Atm


class AtmAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'active')
    list_filter = ('active',)


admin.site.register(Atm, AtmAdmin)
    

