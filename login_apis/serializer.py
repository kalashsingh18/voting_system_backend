from rest_framework import serializers
from .models import users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Users_models_serializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = "__all__"
class CustomUserSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, users):
        
        token = super().get_token(users)
        # Add custom claims
        token['username'] = users.username
        return token
