from django.contrib import admin
from core.models import Goal, DailyRecord

# Register your models here.
admin.site.register(Goal)
admin.site.register(DailyRecord)