from rest_framework import serializers,exceptions
from rest_framework.serializers import ModelSerializer,ValidationError
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model, authenticate
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
  class Meta:
    model = CustomUser
    fields = [
      "email",
      "password",
    ]
    

  # def create(self, validated_data):
  #   user = CustomUser.objects.get(
  #     validated_data["email"],
  #     validated_data["password"]
  #   )

  #   return user

class CustomLoginSerializer(LoginSerializer):
    username = None

    def authenticate(self, **options):
        return authenticate(self.context["request"], **options)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(
                email=email,
                password=password,
            )
            print(email,password)
            if not user:
                msg = "Incorrect credentials."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = "No email provided."
            raise exceptions.ValidationError(msg)
        attrs["user"] = user
        return attrs
