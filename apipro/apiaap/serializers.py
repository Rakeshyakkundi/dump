from rest_framework import serializers
from .models import imagestore

class imagestoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagestore
        fields = "__all__"