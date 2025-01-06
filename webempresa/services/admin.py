from django.contrib import admin
from . import models
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(models.ServiceDB, ProjectAdmin)

