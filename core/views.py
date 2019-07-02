from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django. contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Goal, DailyRecord
from django.views import View
from django.views.generic import DetailView, CreateView

# Create your views here.

def index(request):
    return render(request, 'index.html')
