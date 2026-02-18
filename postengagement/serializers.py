from rest_framework import serializers
from postengagement.models import User,Post,Comment,Like

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['id','username','email','password',"phone"]

    def create(self, data):
        return User.objects.create_user(**data)
    
class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only = True)
    comments = serializers.SerializerMethodField(read_only = True)
    class Meta:

        model = Post

        fields = "__all__"

        read_only_fields = ["id","user","created_at"]

    def get_comments(self,object):
        
        message = Comment.objects.filter(post = object)

        serializer_instance = CommentSerializer(message,many=True)

        return serializer_instance.data  
    
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:

        model = Comment

        fields = "__all__"

        read_only_fields = ["id","user","post","created_at"]

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:

        model = Like

        fields = "__all__"

        read_only_fields = ["id","created_at","user"]

