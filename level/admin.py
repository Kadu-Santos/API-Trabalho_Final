from django.contrib import admin
from level.models import Level

class Nivel(admin.ModelAdmin):
    list_display = ('nivel', 'assunto')
    list_display_links = ('nivel', 'assunto')
    search_fields = ('nivel', 'assunto')

admin.site.register(Level, Nivel)