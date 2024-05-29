from rest_framework import serializers
from .models import mediaDB

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = mediaDB
        fields = '__all__' 
        # For fields field = ('descrion','condition')