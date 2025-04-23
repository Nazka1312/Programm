from django.db import models
from django.contrib.auth.models import User
from .utils import generate_caption, speak


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question_text = models.CharField(max_length=255, blank=True, null=True)
    correct_answer = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='exercises/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text or "Без текста"

    def save(self, *args, **kwargs):
        if self.image and not self.question_text:
            caption = generate_caption(self.image.path)
            self.question_text = caption
        super().save(*args, **kwargs)
