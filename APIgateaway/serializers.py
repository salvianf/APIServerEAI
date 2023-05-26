from rest_framework import serializers
# Create your views here.


class JobSerializer(serializers.Serializer):
    type = serializers.CharField()
    date = serializers.DateField()
    location = serializers.CharField()
    company = serializers.CharField()
