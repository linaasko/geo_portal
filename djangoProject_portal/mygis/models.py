from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

# Create your models here.
