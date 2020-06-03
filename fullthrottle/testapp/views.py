from django.shortcuts import render
from testapp.models import UserModel,ActivityPeroidModel
from testapp.serializers import UserSerializer, ActivitySerializer
from rest_framework import generics


# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer 

class ActivityListView(generics.ListAPIView):
    queryset = ActivityPeroidModel.objects.all()
    serializer_class = ActivitySerializer