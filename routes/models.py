from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Название маршрута
    start_point = models.CharField(max_length=255)  # Стартовая точка (адрес или координаты)
    end_point = models.CharField(max_length=255)  # Конечная точка
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.user.username}"