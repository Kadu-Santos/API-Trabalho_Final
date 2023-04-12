from django.urls import path, include
from rest_framework import routers
from level.views import LevelViewsets, NumNiveisView, LevelQuestionsView

router = routers.DefaultRouter()
router.register(r'', LevelViewsets)

urlpatterns = [
    path('niveis/', NumNiveisView.as_view()),
    path('perguntas/<int:nivel>/', LevelQuestionsView.as_view()),
    path('', include(router.urls)),
]
