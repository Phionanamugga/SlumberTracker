from rest_framework import serializers
from .models import SleepSession

class SleepSessionSerializer(serializers.ModelSerializer):
    duration_hours = serializers.ReadOnlyField()

    class Meta:
        model = SleepSession
        fields = ["id", "start_time", "end_time", "duration_hours"]

