from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'pin']

    def validate(self, data):
        # Validate that passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        
        # Validate PIN (if provided)
        pin = data.get('pin')
        if pin and (not pin.isdigit() or len(pin) != 6):
            raise serializers.ValidationError("PIN must be a 6-digit numeric value")
        
        return data

    def create(self, validated_data):
        # Remove confirm_password since it is not part of the User model
        validated_data.pop('confirm_password')
        
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            pin=validated_data.get('pin')
        )
        return user

