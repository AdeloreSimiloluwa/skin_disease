from rest_framework import serializers

from .models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'disease', 'causes', 'things_to_avoid', 'created_at', 'updated_at']
        