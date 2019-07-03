from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django. contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Goal, DailyRecord
from django.views import View
from django.views.generic import DetailView, CreateView
from django import forms

# Create your views here.

def index(request):
    goals = Goal.objects.all()
    return render(request, 'index.html')

def GoalDetailView(request, pk):
    dailyrecords = DailyRecord.objects.all()
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            render(request, 'index.html/')
    else:
        form = GoalForm()
    return render(request, 'goal-detail.html')
