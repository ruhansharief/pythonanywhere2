from testapp.models import UserModel, ActivityPeroidModel
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeroidModel
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(read_only=True,many=True)
    class Meta:
        model = UserModel
        fields = '__all__'

