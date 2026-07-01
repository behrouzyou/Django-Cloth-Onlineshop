from rest_framework import serializers
from core.model.navigation import Navigation
class NavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Navigation
        fields='__all__'