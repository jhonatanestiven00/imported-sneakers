from django.contrib import admin
from .models import PageDB
# Register your models here.

class pageAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('title','order')

admin.site.register(PageDB, pageAdmin)