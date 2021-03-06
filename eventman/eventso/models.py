from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=150)
    short=models.CharField(max_length=50)
    content=models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    event_date =models.DateTimeField(blank=True, null=True)
    image = models.ImageField(default="default.jpg",upload_to='event_banner')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
