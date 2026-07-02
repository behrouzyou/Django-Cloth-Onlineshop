from django.urls import path

from web.view.home_view import HomeView

urlpatterns = [
    path('', HomeView.as_view())
]
