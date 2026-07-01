from rest_framework import serializers
from core.model.sidebar import Slider
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Slider
        fields='__all__'