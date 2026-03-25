from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    green_credits = models.IntegerField(default=0)
    total_co2_saved_kg = models.FloatField(default=0.0)

    trust_score = models.FloatField(default=1.0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username