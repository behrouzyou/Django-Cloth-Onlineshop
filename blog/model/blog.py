from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from products.model.product import Product


class Blog(models.Model):
    title=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    guest_id=models.CharField(max_length=255,null=True,blank=True)
    content=RichTextField()
    image=models.ImageField(upload_to='static/blog')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    visit_count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return  self.title