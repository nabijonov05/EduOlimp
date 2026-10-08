from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SystemSettings(models.Model):
    total_questions = models.IntegerField(default=30)
    test_duration = models.IntegerField(default=60) 
    default_points = models.IntegerField(default=4)

    class Meta:
        verbose_name = "Tizim sozlamasi"
        verbose_name_plural = "Tizim sozlamalari"

    def __str__(self):
        return "Tizim sozlamalari"
