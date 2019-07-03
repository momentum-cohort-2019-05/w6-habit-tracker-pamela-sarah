from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django. contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Goal, DailyRecord
from django.views import View
from django.views.generic import DetailView, CreateView
from .forms import DailyRecordForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

class GoalDetailView(DetailView):
    model = Goal
    
def create_record(request, goal_pk):
    goal = get_object_or_404(Goal, pk=goal_pk)

    if request.method == "POST":
        form = DailyRecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.goal = goal
            messages.success(request, "Your goal was updated successfully")
            return redirect('goal-detail', pk=goal.pk)
    else:
        form = DailyRecordForm()

    return render(request, 'create_record.html', {
        "goal": goal,
        "form": form
    })