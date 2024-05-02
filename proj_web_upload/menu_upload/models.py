from django.db import models

# Create your models here.
class Photo(models.Model):
    owner_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
