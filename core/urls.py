from django.urls import include,path
from rest_framework.routers import DefaultRouter

from core.view.navigation_view_set import NavigationViewSet
from core.view.slider_view_set import SliderViewSet

router=DefaultRouter()
router.register('slider',SliderViewSet)
router.register('navigation',NavigationViewSet)
urlpatterns=[
    path('',include(router.urls)),
]