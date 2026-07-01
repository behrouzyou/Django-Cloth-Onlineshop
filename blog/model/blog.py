from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from products.model.product import Product


class Blog(models.Model):
    title=models.CharField(max_length=255)
    content=RichTextField()
    image=models.ImageField(upload_to='static/blog')
    is_published=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    visit_count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return  self.title