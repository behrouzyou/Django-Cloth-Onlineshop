from django.urls import path

from web.view.about_view import AboutView
from web.view.home_view import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('about-us/', AboutView.as_view()),
]
