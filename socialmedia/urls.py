"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from postengagement.views import SignUpView,PostCreateListView,PostRetrieveView,PostDeleteView,CommentCreateView,LikeCreateView
from rest_framework.authtoken.views  import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',SignUpView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
    path('post/',PostCreateListView.as_view()),
    path('post/<int:pk>/',PostRetrieveView.as_view()),
    path('post/<int:pk>/remove/',PostDeleteView.as_view()),
    path('post/<int:pk>/add-comment/',CommentCreateView.as_view()),
    path('post/<int:pk>/like/',LikeCreateView.as_view()),

]
