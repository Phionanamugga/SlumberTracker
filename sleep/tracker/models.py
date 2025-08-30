from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class SleepSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sleep_sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-start_time"]

    def __str__(self):
        return f"{self.user.username} slept at {self.start_time} – woke {self.end_time}"

    @property
    def duration_hours(self):
        if self.end_time and self.start_time:
            return round((self.end_time - self.start_time).total_seconds() / 3600, 2)
        return 0
