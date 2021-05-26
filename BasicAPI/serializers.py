from rest_framework import serializers
from .models import ApiModel


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = '__all__'
