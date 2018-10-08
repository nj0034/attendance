import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import AttendanceUser
from datetime import datetime, timedelta


class Week(models.Model):
    week_start = models.DateField(verbose_name="한 주 시작 날짜")
    week_end = models.DateField(verbose_name="한 주 종료 날짜")

    def in_week(self, current_datetime):
        if self.week_start <= current_datetime.date() <= self.week_end:
            return True
        return False

    @classmethod
    def find_week(cls, current_datetime=None):
        if current_datetime is None:
            current_datetime = datetime.today()

        weekday = current_datetime.weekday()
        week_start = current_datetime - timedelta(weekday)
        week_end = current_datetime + timedelta(6 - weekday)

        week = cls.objects.get_or_create(week_start=week_start, week_end=week_end)
        return week[0]

    def __str__(self):
        return "{} ~ {}".format(self.week_start, self.week_end)


class WeekSubject(models.Model):
    id = models.UUIDField(verbose_name="UUID", primary_key=True, default=uuid.uuid4, editable=False)
    week = models.ForeignKey('Week', on_delete=models.CASCADE)
    professor = models.ForeignKey('accounts.AttendanceUser', on_delete=models.CASCADE, related_name='subject_professor')
    name = models.CharField(max_length=200)
    # day_subjects = models.ManyToManyField('DaySubject')
    students = models.ManyToManyField('accounts.AttendanceUser', related_name='subject_students')
    default = models.BooleanField(default=False)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

    def __str__(self):
        return "[{}] {}({})".format(self.week, self.name, self.professor)

    def set_students(self, student_list):
        if student_list:
            for student_name in student_list:
                student = AttendanceUser.objects.get(name=student_name, type='student')
                self.students.add(student)

    def find_day_subject(self):
        day_subjects = self.day_subjects.all()

        for day_subject in day_subjects:
            if day_subject.day == datetime.today().weekday():
                return day_subject


class DaySubject(models.Model):
    DAY = (
        (0, '월'),
        (1, '화'),
        (2, '수'),
        (3, '목'),
        (4, '금'),
    )
    TIME = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7))

    week_subject = models.ForeignKey('WeekSubject', on_delete=models.CASCADE, related_name='day_subjects')
    day = models.IntegerField(choices=DAY)
    time = models.IntegerField(choices=TIME)

    def __str__(self):
        return "{} {} {}교시".format(self.week_subject, self.get_day_display(), self.time)

    def __repr__(self):
        return "{} {} {}교시".format(self.week_subject, self.get_day_display(), self.time)


@receiver(post_save, sender=Week)
def create_week_subject(sender, instance, created, **kwargs):
    if created:
        week_subjects = WeekSubject.objects.filter(default=True)

        for week_subject in week_subjects:
            professor = week_subject.professor
            day_subjects = week_subject.day_subjects.all()
            students = week_subject.students.all()

            week_subject.id = None
            week_subject.professor = professor
            week_subject.week = instance
            week_subject.default = False
            # week_subject._day_subjects = day_subjects
            week_subject.save()

            week_subject.students.add(*students)

            for day_subject in day_subjects:
                day_subject.id = None
                day_subject.week_subject = week_subject
                day_subject.save()


# @receiver(post_save, sender=WeekSubject)
# def create_week_subject(sender, instance, created, **kwargs):
#     if created:
#         day_subjects = instance._day_subjects
#
#         for day_subject in day_subjects:
#             day_subject.id = None
#             day_subject.week_subject = instance
#             day_subject.save()

