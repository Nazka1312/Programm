from django.contrib import admin
from .models import Exercise

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id']  # Укажи только существующие поля
    readonly_fields = []  # Или удали эту строку совсем, если не нужно