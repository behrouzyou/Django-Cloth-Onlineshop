from django.db import models
class Slider(models.Model):
    title=models.CharField(max_length=255,verbose_name='عنوان')
    subtitle=models.CharField(max_length=255,verbose_name='زیرنویس')
    link=models.URLField(verbose_name='لینک')
    is_active=models.BooleanField(default=True,verbose_name='فعال')
    image=models.ImageField(upload_to='static/sliders/',verbose_name='تصویر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'