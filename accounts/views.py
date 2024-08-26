from rest_framework import generics
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print("user is: ",user)
        token,created = Token.objects.get_or_create(user=user)
        print("token is ",token)
        print("created is ",created)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'username':user.username
        })


class UserLoginView(APIView):
    def post(self,request):
        user = authenticate(username=request.data['username'],password=request.data['password'])
        print(request.data['username'])
        print(request.data['password'])
        if user:
            token,created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=401)