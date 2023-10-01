from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    # Set fields as not required by setting required=False
    profile_picture = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)
    location = serializers.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = [ 'contact_number', 'profile_picture', 'bio', 'location']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    def create(self, validated_data):
        # password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        # Check if a password is provided and hash it
        # if password is not None:
        #     instance.password = make_password(password)
        
        instance.save()
        return instance
