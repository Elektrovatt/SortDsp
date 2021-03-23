from django.contrib import admin

# Register your models here.

from .models import *

class table_thickness_ground_plate_modelAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date_created')
    list_display_links = ('id', 'author')
    search_fields = ('author', )

admin.site.register(table_thickness_ground_plate_model, table_thickness_ground_plate_modelAdmin)