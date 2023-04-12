from rest_framework import viewsets
from questions.models import Pergunta, Puzzle
from questions.serializer  import PerguntaSerializer, PuzzleSerializer


# A viewset é uma classe que contém os métodos necessários para responder a diferentes solicitações
# HTTP, como GET, POST, PUT e DELETE, entre outras. O ModelViewSet é um tipo de viewset que fornece
# implementações padrão para os métodos HTTP mais comuns.

class PerguntaViewsets(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class PuzzleViewsets(viewsets.ModelViewSet):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzleSerializer