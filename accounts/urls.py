from .views import RegisterAPI 
from django.urls import path, include
from knox import views as knox_views
from .views import LoginAPI, ChangePasswordView, UserAPI
from accounts.views import RespostaViewsets, QuestoesRespondidasView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'respostas', RespostaViewsets)

urlpatterns = [ 
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/', UserAPI.as_view()),
    path('respondidas/', QuestoesRespondidasView.as_view()),
    path('', include(router.urls))
]