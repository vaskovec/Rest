from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet


class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json.pop('password')
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(ModelViewSet):
    """ 
    User profile. 
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
