

# Register your models here.
from django.contrib import admin
from .models import SleepSession

@admin.register(SleepSession)
class SleepAdmin(admin.ModelAdmin):
    list_display = ("user", "start_time", "end_time", "duration_hours")
    search_fields = ("user__username",)
    list_filter = ("user",)
