from django.contrib.auth.models import AbstractUser
from questions.models import Pergunta, Puzzle
from django.db import models

class CustomUser(AbstractUser):
    # adicionando um campo de nivel
    level = models.IntegerField(default = 0)

class Resposta(models.Model):
    rusuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rpergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, null=True)
    rpuzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, null=True)
    rrespondido_em = models.DateTimeField(auto_now_add=True)
