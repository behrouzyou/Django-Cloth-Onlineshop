from django.db import models
class Slider(models.Model):
    title=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    link=models.URLField()
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='static/sliders/')
    def __str__(self):
        return self.title