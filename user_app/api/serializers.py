from rest_framework import serializers
from user_app.models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['uid', 'username', 'email','favoriteResort']
        extra_kwargs = {
            'uid': {'required': True},
            'username': {'required': True},
            'email': {'required': True},
            'favoriteResort': {'required': True},
        }

    def create(self, validated_data):
        if CustomUser.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})
        if CustomUser.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'Username already exists!'})

        user = CustomUser.objects.create(
            uid=validated_data['uid'],
            username=validated_data['username'],
            email=validated_data['email'],
            favoriteResort=validated_data['favoriteResort'],
        )
        user.save()
        return user
