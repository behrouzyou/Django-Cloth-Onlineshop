from rest_framework.viewsets import ReadOnlyModelViewSet

from core.model.serializer.slider_serializer import SliderSerializer
from core.model.slider import Slider


class SliderViewSet(ReadOnlyModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
