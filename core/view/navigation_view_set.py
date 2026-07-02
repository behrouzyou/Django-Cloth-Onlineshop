from rest_framework.viewsets import ReadOnlyModelViewSet

from core.model.navigation import Navigation
from core.model.serializer.navigation_serializer import NavigationSerializer


class NavigationViewSet(ReadOnlyModelViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer
