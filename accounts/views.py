from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

from rest_framework import generics, permissions

# Change Password
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from accounts.models import Resposta
from accounts.serializers import RespostaSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from accounts.models import Resposta

class RespostaViewsets(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer

from django.forms.models import model_to_dict
from django.http import JsonResponse

class QuestoesRespondidasView(APIView):
    def get(self, request, format=None):
        # Verifica se o usuário está autenticado
        if not request.user.is_authenticated:
            return Response({'message': 'Usuário não autenticado'})

        # Recupera o usuário logado
        usuario = request.user

        # Filtra as respostas do usuário e as ordena pela data de resposta
        respostas = Resposta.objects.filter(rusuario_id=usuario.id).order_by('-rrespondido_em')

        # Cria listas vazias para as perguntas e puzzles
        perguntas = []
        puzzles = []

        # Itera sobre as respostas filtradas e adiciona as perguntas e puzzles às listas correspondentes
        for resposta in respostas:
            if resposta.rpergunta:
                perguntas.append(model_to_dict(resposta.rpergunta))
            if resposta.rpuzzle:
                puzzles.append(model_to_dict(resposta.rpuzzle))

        # Retorna a lista de perguntas e puzzles concatenadas
        return Response({'perguntas': perguntas, 'puzzles': puzzles})

