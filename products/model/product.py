from ckeditor.fields import RichTextField
from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=RichTextField()
    price=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='static/products')
    stock=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    visit_count=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name