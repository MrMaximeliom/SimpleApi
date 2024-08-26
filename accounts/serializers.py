from rest_framework import  serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=False)

    class Meta:
        model = User
        fields = ['id','username','email','name','password']

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.name = validated_data.get('name',instance.name)
        password = validated_data.get('password',None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance