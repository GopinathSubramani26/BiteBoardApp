from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length = 8, style={'input_type': 'password'})
    confirm_password = serializers.CharField(wrire_only = True, style = {'input_type': 'password'})

class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'pin']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            email= validated_data['email'],
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username=validated_data.get('email'),
            pin = validated_data.get('pin')
        )
        return user