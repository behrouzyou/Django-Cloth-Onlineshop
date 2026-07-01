from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from products.model.product import Product


class Blog(models.Model):
    title=models.CharField(max_length=255,verbose_name='عنوان')
    content=RichTextField(verbose_name='محتوا')
    image=models.ImageField(upload_to='static/blog',verbose_name='تصویر')
    is_published=models.BooleanField(default=True,verbose_name='وضعیت انتشار')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='ایجاد')
    updated_at=models.DateTimeField(auto_now_add=True,verbose_name='ویرایش')
    visit_count=models.PositiveIntegerField(default=0,verbose_name='بازدید')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural="بلاگ"