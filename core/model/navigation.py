from django.db import models


class Navigation(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    link = models.URLField(verbose_name='لینک')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک'
        verbose_name_plural = 'لینک‌ها'
