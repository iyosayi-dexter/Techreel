from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    twitter_handle = models.CharField(max_length=50 , default='@iyosayi18')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
