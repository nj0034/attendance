from django.contrib import admin
from .models import Week, WeekSubject, DaySubject


class WeekSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'week', 'name', 'professor')
    ordering = ('week', 'professor', 'name')


admin.site.register(Week)
admin.site.register(WeekSubject, WeekSubjectAdmin)
admin.site.register(DaySubject)
