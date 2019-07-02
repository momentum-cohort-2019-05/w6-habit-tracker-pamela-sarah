from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Goal(models.Model):
    name = models.CharField(max_length=500, help_text= "Enter your goal here")
    description = models.TextField(help_text="Enter the decription of your goal here")
    date_added = models.DateField(auto_now_add=True)
    daily_target = models.IntegerField(help_text = "Enter a target number for your goal(i.e. 1,000 step per day")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date_added"]

    def __str__(self):
        return self.name
   

class DailyRecord(models.Model):
    date_added = models.DateField(auto_now_add=True)
    progress = models.IntegerField(help_text = "Enter your progress here")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Goal, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'progress']
        ordering = ['-date_added']

    
    def __str__(self):
        return self.progress

    

