from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import authentication,permissions,serializers
from  postengagement.serializers import UserSerializer,PostSerializer,CommentSerializer,LikeSerializer
from postengagement.models import Post,Like
from postengagement.permissions import IsOwner
class SignUpView(CreateAPIView):

    serializer_class = UserSerializer

class PostCreateListView(ListCreateAPIView):

    serializer_class = PostSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)

    def get_queryset(self):
        
        return Post.objects.all()
    
class PostRetrieveView(RetrieveAPIView):

    serializer_class = PostSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    queryset = Post.objects.all()  

class PostDeleteView(DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    queryset = Post.objects.all()


class CommentCreateView(CreateAPIView):

    serializer_class = CommentSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        id = self.kwargs.get("pk")

        post_instance = Post.objects.get(id=id)

        serializer.save(post = post_instance,user=self.request.user)

class LikeCreateView(CreateAPIView):

    serializer_class= LikeSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        id = self.kwargs.get("pk")

        post_instance = Post.objects.get(id=id)


        if Like.objects.filter(user=self.request.user, post=post_instance).exists():
            raise serializers.ValidationError("You already liked this post.")

        serializer.save(post = post_instance,user = self.request.user)

        
