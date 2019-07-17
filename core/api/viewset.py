from rest_framework import parsers, renderers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import AuthSerializers
User = get_user_model()


class AuthViewSet(ModelViewSet):

    serializer_class = AuthSerializers
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        return Response({'message': 'Sem permissão'})

    def create(self, request, *args, **kwargs):
        data = request.data
        if User.objects.filter(email=data['email']):
            return Response({'message': 'Usuário já cadastrado'}, status=406)
        else:
            user = User.objects.create(
                username=data['name'].split()[0],
                name=data['name'],
                email=data['email'],
                password=make_password(data['password'])
            )
            token = Token.objects.create(
                user=user
            )
            if token:
                return Response(
                    {
                        'token': token.key,
                        'name': user.get_short_name(),
                        'full_name': user.name,
                        'email': user.email
                    }
                )
            else:
                return Response({
                    'message': 'Erro ao criar usuário'
                })

    def destroy(self, request, *args, **kwargs):
        return Response({'message': 'Sem permissão'})

    def retrieve(self, request, *args, **kwargs):
        return Response({'message': 'Sem permissão'})


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'name': user.get_short_name(),
                'full_name': user.name,
                'email': user.email
            }
        )

