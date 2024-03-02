from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from common.utils import success_response
from user_auth.models import UserProfile
from user_auth.serializers import LoginSerializer, UserProfileSerializer


class LoginViewView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        """
        api for login
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserProfile.exist_username(username=request.data["username"])
        if user:
            if not user.check_password(request.data["password"]):
                raise ValidationError(
                    detail={"user": ["username or password does not match"]}
                )
        else:
            raise ValidationError(detail={"user": ["username does not exists"]})

        data = UserProfileSerializer(user, context={"request": request}).data
        return success_response(
            message="login successfully",
            data=data,
            extra_data={"token": user.get_token()},
        )


class UserSignUpView(GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """
        api from user's signup
        """
        user = UserProfile.exist_username(username=request.data["username"])
        if user:
            raise ValidationError(detail={"user": ["username already exists"]})
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(password=make_password(self.request.data["password"]))
        data = UserProfileSerializer(user, context={"request": request}).data
        return success_response(
            message="signup successfully",
            data=data,
            extra_data={"token": user.get_token()},
            status=status.HTTP_201_CREATED,
        )
