from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.


@api_view(['POST'])
def signUp(request):
    data = request.data
    if 'username' in data and 'password' in data and 'email' in data:
        try:
            user = User.objects.get(username=request.data['username'])
        except:
            # some error occured and the user doesnt exist, create a user in that case
            user = User.objects.create(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data['email'])
            if 'img' in data:
                Profile.objects.create(user=user, img=data['img'])
            token = Token.objects.get(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
                # 'user': user.username,
            }, status=status.HTTP_201_CREATED)
        else:
            # user aldready exists.
            return Response({
                'error': 'user_exists'
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'error': 'invalid_fields'
        })


@api_view(['POST'])
def getToken(request):
    # signIn
    data = request.data
    if 'email' in data and 'password' in data:
        # all valid credentials are there
        try:
            user = User.objects.get(
                email=data['email'], password=data['password'])
        except:
            # the credentials are invalid.
            return Response({'error': 'invalid_credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # success we can send the dem token
            token = Token.objects.get(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)

    else:
        return Response({
            'error': 'invalid_fields'
        }, status=status.HTTP_400_BAD_REQUEST)
