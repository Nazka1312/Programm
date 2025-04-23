from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class SafeZone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Например: Дом, Больница
    address = models.CharField(max_length=255)  # Описание или адрес
    radius_meters = models.PositiveIntegerField(default=100)  # Радиус в метрах
    latitude = models.FloatField()  # Широта
    longitude = models.FloatField()  # Долгота
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"