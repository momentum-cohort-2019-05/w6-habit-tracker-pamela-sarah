from django import forms
from core.models import Goal, DailyRecord

class GoalForm(forms.ModelForm):

    class Meta:
        models = Goal
        fields = ('name','description','daily_target',)


class DailyRecordForm(forms.ModelForm):

    class Meta:
        models = DailyRecord
        fields = ('progress',)