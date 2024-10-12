from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=27, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["full_name", "email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            full_name=validated_data["full_name"],
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=5)
    password = serializers.CharField(max_length=27, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)
        if user and user.is_active:
            return user

        raise serializers.ValidationError("Invalid credentials")
