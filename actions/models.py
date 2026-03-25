from django.db import models
from django.contrib.auth.models import User

class EcoAction(models.Model):
    ACTION_TYPES = [
        ('PLANT_TREE', 'Plant Tree'),
        ('CYCLE', 'Cycle'),
        ('CLEAN_AREA', 'Clean Area'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('VERIFIED', 'Verified'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    action_type = models.CharField(max_length=30, choices=ACTION_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    photo_url = models.URLField()

    latitude = models.FloatField()
    longitude = models.FloatField()

    credits_awarded = models.IntegerField(default=0)
    co2_kg_offset = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action_type}"