from django.contrib import admin
from .models import CustomUser

class User(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'level')
    list_display_links= ('id', 'username', 'email',)
    search_fields = ('username', 'level')

admin.site.register(CustomUser, User)


from accounts.models import Resposta

class Respondidas(admin.ModelAdmin):
    list_display = ('id', 'rusuario', 'rpergunta', 'rpuzzle', 'rrespondido_em')
    list_display_links= ('id', 'rusuario', 'rpergunta', 'rpuzzle')
    search_fields = ('id', 'rusuario')

admin.site.register(Resposta, Respondidas)