from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class userAuthSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    user = userAuthSerializers()

    class Meta:
        model = UserProfile
        fields = ['user', 'role', 'designation', 'phone']