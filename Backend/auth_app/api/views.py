from rest_framework import status, permissions
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class RegistrationView(APIView):
    permission_classes = [permissions.AllowAny] 

    def post(self, request, *args, **kwargs):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {'detail': 'Ungültige Anfragedaten.'},
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            data = {}
            if serializer.is_valid():
                saved_account = serializer.save()
                token, created = Token.objects.get_or_create(user=saved_account)
                data = {
                    'token': token.key,
                    'fullname': saved_account.fullname,
                    'email': saved_account.email,
                    'user_id': saved_account.id,
                }
                return Response(
                    data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'detail': 'Interner Serverfehler.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
class LoginView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]  
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'fullname': user.fullname,
                'email': user.email,
                'user_id': user.id,
            }
            return Response(data, {'detail': 'Erfolgreiche Anmeldung.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'detail': 'Interner Serverfehler.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )