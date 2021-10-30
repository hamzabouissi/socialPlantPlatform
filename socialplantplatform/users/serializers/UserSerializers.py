from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "name", "image"]



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "email", "name","image", "password",]

        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate_password(self, value):
        password = make_password(value)
        return password



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        valid = User.objects.authenticate_user(attrs['username'], attrs['password'])
        if not valid:
            raise serializers.ValidationError("Username or Password may be wrong")
        return attrs


class ProfileSerializer(serializers.Serializer):
    publications = serializers.IntegerField()
    am_follow = serializers.IntegerField()
    follow_me = serializers.IntegerField()
