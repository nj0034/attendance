from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from subjects.models import DaySubject


class AttendanceNumber(models.Model):
    number = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    day_subject = models.ForeignKey('subjects.DaySubject', on_delete=models.CASCADE)


class AttendanceInfo(models.Model):
    STATE = (
        (0, ''),
        (1, '출석'),
        (2, '지각'),
        (3, '이탈'),
        (4, '결석'),
    )

    student = models.ForeignKey('accounts.AttendanceUser', on_delete=models.CASCADE)
    day_subject = models.ForeignKey('subjects.DaySubject', on_delete=models.CASCADE)
    state = models.IntegerField(choices=STATE, default=0)


@receiver(post_save, sender=DaySubject)
def create_week_subject(sender, instance, created, **kwargs):
    if created:
        students = instance.week_subject.students.all()

        for student in students:
            AttendanceInfo.objects.create(student=student, day_subject=instance)
