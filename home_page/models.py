from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class hotel(models.Model):
    name = models.CharField(max_length= 100)
    area = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='photos/hotels')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    ratting = models.IntegerField()
    comment = models.TextField()

    def __str__(self) -> str:
        return str(self.Hotel)