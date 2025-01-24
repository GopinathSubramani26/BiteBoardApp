from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework import APIView
from rest_framework.response import Response
from django.urls import path

from biteboard.api.serializer import UserSerializer
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
