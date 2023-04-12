from django.urls import path, include
from rest_framework import routers
from questions.views import PerguntaViewsets, PuzzleViewsets

router = routers.DefaultRouter()
router.register(r'perguntas', PerguntaViewsets)
router.register(r'puzzles', PuzzleViewsets)

urlpatterns = [
    path('', include(router.urls))
]