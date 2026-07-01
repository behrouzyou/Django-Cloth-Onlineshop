from rest_framework import  viewsets

from core.model.serializer.slider_serializer import SliderSerializer
from core.model.sidebar import Slider

class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer