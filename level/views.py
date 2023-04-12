from rest_framework import viewsets
from level.models import Level
from level.serializer  import LevelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class LevelViewsets(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    

class NumNiveisView(APIView):
    def get(self, request, format=None):
        num_niveis = Level.objects.count()
        return Response({'num_niveis': num_niveis})
    
from rest_framework.views import APIView
from rest_framework.response import Response
from level.models import Level
from questions.models import Pergunta, Puzzle
from questions.serializer import PerguntaSerializer, PuzzleSerializer
from django.shortcuts import get_object_or_404


class LevelQuestionsView(APIView):
    def get(self, request, nivel, format=None):
        # Recupera o objeto Level pelo número do nível
        level = get_object_or_404(Level, nivel=nivel)

        # Filtra as perguntas e puzzles pelo nível
        perguntas = Pergunta.objects.filter(perguntaNivel=level)
        puzzles = Puzzle.objects.filter(puzzleNivel=level)

        # Serializa as perguntas e puzzles
        perguntas_serializer = PerguntaSerializer(perguntas, many=True)
        puzzles_serializer = PuzzleSerializer(puzzles, many=True)

        # Retorna a lista de perguntas e puzzles concatenadas
        return Response(perguntas_serializer.data + puzzles_serializer.data)

