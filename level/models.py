from django.db import models

class Level(models.Model):
    nivel = models.IntegerField(primary_key=True)
    assunto = models.CharField(max_length=250)
    explicacao = models.CharField(max_length=1000)

    def __str__(self):
        return self.assunto
