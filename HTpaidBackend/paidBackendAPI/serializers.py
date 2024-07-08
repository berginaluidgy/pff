from rest_framework import serializers
from .models import User
from .models import Career, Mission, uploadVideo, socialaccess


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password','date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class UploadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadVideo
        fields = '__all__'

class SocialAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = socialaccess
        fields = '__all__'