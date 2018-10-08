from django.contrib import admin
from .models import AttendanceUser


class AttendanceUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)


admin.site.register(AttendanceUser, AttendanceUserAdmin)

# Register your models here.
