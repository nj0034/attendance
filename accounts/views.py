from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AttendanceUser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class SignUp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            type = request.data.get('type')

            user = User.objects.create(username=username, password=password)
            token = Token.objects.create(user=user)

            AttendanceUser.objects.create(user=user, type=type, name=username)

            data = {
                "token": token.key,
                "name": username,
                "type": type
            }

            print(data)

            return Response(status=status.HTTP_201_CREATED, data=data)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": str(e)})


class SignIn(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        if request.user.is_authenticated:
            attendanceuser = request.user.attendanceuser
            token = Token.objects.get(user=request.user)
            data = {
                "token": token.key,
                "id": attendanceuser.id,
                "name": attendanceuser.name,
                "type": attendanceuser.type
            }
            return Response(status=status.HTTP_200_OK, data=data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            attendanceuser = user.attendanceuser
            token = Token.objects.get(user=user)
            data = {
                "token": token.key,
                "id": attendanceuser.id,
                "name": attendanceuser.name,
                "type": attendanceuser.type
            }

            return Response(status=status.HTTP_200_OK, data=data)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


