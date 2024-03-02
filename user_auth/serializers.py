from rest_framework import serializers

from user_auth.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "first_name",
            "last_name",
            "password",
            "username",
        )

    def to_representation(self, instance):
        """removing password hash from response"""
        data = super(UserProfileSerializer, self).to_representation(instance)
        data.pop("password")
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
