from rest_framework import serializers
from postengagement.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['id','username','email','password',"phone"]

    def create(self, data):
        return User.objects.create_user(**data)