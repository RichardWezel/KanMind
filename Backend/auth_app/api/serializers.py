from rest_framework import serializers
from django.contrib.auth.models import User
from auth_app.models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):

    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        validated_data = self.validated_data
        pw = self.validated_data['password']
        repeat_pw = self.validated_data['repeated_password']
        
        if pw != repeat_pw:
            raise serializers.ValidationError("Passwords do not match.")
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        
        account = User(
            username=validated_data['fullname'],
            email=validated_data['email']
        )
        
        account.set_password(pw) 
        account.save()
        return account


