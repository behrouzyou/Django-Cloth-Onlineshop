from django.db import models
class Navigation(models.Model):
    title=models.CharField(max_length=255)
    link=models.URLField()
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.title