from django.contrib import admin

# Register your models here.

from .models import *

class Thickness_board_model_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date_created')
    list_display_links = ('id', 'author')
    search_fields = ('author', )
admin.site.register(Thickness_board_model, Thickness_board_model_Admin)


class Thickness_pack_board_model_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date_created')
    list_display_links = ('id', 'author')
    search_fields = ('author', )
admin.site.register(Thickness_pack_board_model, Thickness_pack_board_model_Admin)


class Thickness_unpolished_board_model_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date_created')
    list_display_links = ('id', 'author')
    search_fields = ('author', )
admin.site.register(Thickness_unpolished_board_model, Thickness_unpolished_board_model_Admin)


class Thickness_unpolished_pack_board_model_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date_created')
    list_display_links = ('id', 'author')
    search_fields = ('author', )

admin.site.register(Thickness_unpolished_pack_board_model, Thickness_unpolished_pack_board_model_Admin)


class Number_tapes_model_Admin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date_created')
    list_display_links = ('id', 'author')
    search_fields = ('author', )

admin.site.register(Number_tapes_model, Number_tapes_model_Admin)