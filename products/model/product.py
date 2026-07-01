from ckeditor.fields import RichTextField
from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=255,verbose_name='نام')
    description=RichTextField(verbose_name='توضیحات')
    price=models.PositiveIntegerField(verbose_name='قیمت')
    is_active=models.BooleanField(default=True,verbose_name='فعال')
    image=models.ImageField(upload_to='static/products',verbose_name='تصویر')
    stock=models.PositiveIntegerField(verbose_name='تعداد')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='ایجاد')
    updated_at=models.DateTimeField(auto_now_add=True,verbose_name='ویرایش')
    visit_count=models.PositiveIntegerField(default=0,verbose_name='بازدید')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'