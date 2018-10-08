from django.contrib import admin
from .models import AttendanceNumber, AttendanceInfo


class AttendanceNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'day_subject', 'created_datetime')


class AttendanceInfoAdmin(admin.ModelAdmin):
    list_display = ('day_subject', 'student', 'state')


admin.site.register(AttendanceNumber, AttendanceNumberAdmin)
admin.site.register(AttendanceInfo, AttendanceInfoAdmin)
