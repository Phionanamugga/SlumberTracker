
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SleepSessionForm
from .models import SleepSession

@login_required
def dashboard(request):
    sessions = SleepSession.objects.filter(user=request.user)
    avg_sleep = round(sum(s.duration_hours for s in sessions) / len(sessions), 2) if sessions else 0
    return render(request, "tracker/dashboard.html", {"sessions": sessions, "avg_sleep": avg_sleep})

@login_required
def add_sleep(request):
    if request.method == "POST":
        form = SleepSessionForm(request.POST)
        if form.is_valid():
            sleep = form.save(commit=False)
            sleep.user = request.user
            sleep.save()
            return redirect("dashboard")
    else:
        form = SleepSessionForm()
    return render(request, "tracker/add_sleep.html", {"form": form})

@login_required
def delete_sleep(request, pk):
    sleep = get_object_or_404(SleepSession, pk=pk, user=request.user)
    sleep.delete()
    return redirect("dashboard")
