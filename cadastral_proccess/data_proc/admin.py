from django.contrib import admin

from .models import CadastralData


@admin.register(CadastralData)
class CadastralDataAdmin(admin.ModelAdmin):
    list_display = ('cadastral_number', 'longitude',
                    'latitude', 'result', 'date')
    list_filter = ('cadastral_number', 'longitude', 'latitude', 'result')
    search_fields = ('cadastral_number', 'longitude', 'latitude', 'result')
    empty_value_display = '-пусто-'
