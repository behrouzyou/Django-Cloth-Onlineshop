from django.urls import path

from web.view.about_view import AboutView
from web.view.blog_view import BlogListView
from web.view.home_view import HomeView
from web.view.product_veiw import ProductView
from web.view.products_view import ProductListView
from web.view.single_blog_view import SingleBlogView

urlpatterns = [
    path('', HomeView.as_view()),
    path('product/<int:pk>/',ProductView.as_view()),
    path('products/',ProductListView.as_view()),
    path('blog/',BlogListView.as_view()),
    path('blog/<int:pk>/',SingleBlogView.as_view()),
    path('about-us/',AboutView.as_view()),
]
