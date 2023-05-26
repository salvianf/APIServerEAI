from rest_framework import serializers
# Create your views here.


class JobSerializer(serializers.Serializer):
    type = serializers.CharField()
    date = serializers.CharField()
    location = serializers.CharField()
    company = serializers.CharField()
