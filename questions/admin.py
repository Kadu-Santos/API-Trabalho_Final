from django.contrib import admin
from questions.models import Pergunta, Puzzle

class Questao(admin.ModelAdmin):
    list_display = ('id', 'perguntaNivel', 'pergunta', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'presposta')
    list_display_links = ('id', 'perguntaNivel', 'pergunta', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'presposta')
    search_fields = ('pergunta', 'perguntaNivel')

class GamePuzzle(admin.ModelAdmin):
    list_display = ('id', 'puzzleNivel', 'puzzleEnunciado', 'puzzleComand', 'puzzleResposta')
    list_display_links= ('id', 'puzzleNivel', 'puzzleEnunciado')
    search_fields = ('id', 'puzzleNivel', 'puzzleEnunciado')

#Adicionando o registro de questões a area administrativa primeiro
# parametro o modelo que está sendo usado, segundo o que foi criado logo acima
admin.site.register(Pergunta, Questao)
admin.site.register(Puzzle, GamePuzzle)