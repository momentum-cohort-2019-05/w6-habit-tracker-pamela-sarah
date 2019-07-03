from django import forms
from core.models import Goal, DailyRecord

class GoalForm(forms.ModelForm):
    pass

class DailyRecordForm(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = (
            'progress',
        )