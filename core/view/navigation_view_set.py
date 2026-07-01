from rest_framework import viewsets
from core.model.navigation import Navigation
from core.model.serializer.navigation_serializer import NavigationSerializer


class NavigationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer