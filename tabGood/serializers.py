from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class CountSerializer(serializers.Serializer):
    count = serializers.DecimalField(max_digits=5, decimal_places=2)
