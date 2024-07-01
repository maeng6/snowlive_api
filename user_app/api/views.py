from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.models import User
from rest_framework import generics
from firebase_admin import auth
from user_app.api.serializers import RegistrationSerializer

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        # token = request.data.get('firebase_token')
        # try:
        #     decoded_token = auth.verify_id_token(token)
        #     uid = decoded_token['uid']
        # except Exception as e:
        #     return Response({'error': 'Invalid Firebase token'}, status=status.HTTP_400_BAD_REQUEST)
        # request.data['uid'] = uid
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
