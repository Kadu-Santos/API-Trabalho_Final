from django.db import models
from level.models import Level

#Classe/tabela de pergutas e respostas
class Pergunta(models.Model):
    perguntaNivel = models.ForeignKey(Level, on_delete=models.CASCADE, default = 0)
    pergunta = models.CharField(max_length=250)
    alternativa_a = models.CharField(max_length=250)
    alternativa_b = models.CharField(max_length=250)
    alternativa_c = models.CharField(max_length=250)
    alternativa_d = models.CharField(max_length=250)
    presposta = models.CharField(max_length=250)

    #métodos
    def __str__(self):
        return self.pergunta

    #função define um método chamado __str__ que retorna a pergunta da questão como uma representação
    # em string da instância do modelo. Isso é útil para exibir o modelo de forma legível, por exemplo,
    # em um painel de administração do Django ou em um template HTML.

class Puzzle(models.Model):
    puzzleNivel = models.ForeignKey(Level, on_delete=models.CASCADE, default = 0)
    puzzleEnunciado = models.CharField(max_length=250)
    puzzleComand = models.CharField(max_length=250)
    puzzleResposta = models.CharField(max_length=250)

    def __str__(self):
        return self.puzzleEnunciado

