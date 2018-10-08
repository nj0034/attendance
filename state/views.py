from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AttendanceInfo, AttendanceNumber
from subjects.models import WeekSubject
from accounts.models import AttendanceUser
from .serializer import AttendanceInfoSerializer

import random
from threading import Timer
from django.utils import timezone


def absence_process(**kwargs):
    day_subject = kwargs.get('day_subject')
    attendance_info_list = AttendanceInfo.objects.filter(day_subject=day_subject)

    for attendance_info in attendance_info_list:
        if attendance_info.state == 0:
            attendance_info.state = 4
            attendance_info.save()


class RandomNumber(APIView):
    def post(self, request):
        week_subject_id = request.data.get('id')
        week_subject = WeekSubject.objects.get(id=week_subject_id)

        day_subject = week_subject.find_day_subject()

        if day_subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data="오늘 수업이 없습니다.")

        number = random.randrange(100000, 999999)

        AttendanceNumber.objects.create(day_subject=day_subject, number=number)

        t = Timer(180, absence_process, kwargs={"day_subject": day_subject})
        t.start()

        return Response(status=status.HTTP_201_CREATED, data={"number": number})


class CheckAttendance(APIView):
    def get(self, request):
        subject_name = request.GET.get('subject_name')
        student = request.user.attendanceuser

        week_subjects = WeekSubject.objects.filter(name=subject_name, students=student).order_by('week__week_start')

        attendance_info_list = list()
        for week_subject in week_subjects:
            day_subjects = week_subject.day_subjects.order_by('day')

            for day_subject in day_subjects:
                attendance_info = AttendanceInfo.objects.get(day_subject=day_subject, student=student)

                attendance_info_list.append(
                    {"day": attendance_info.day_subject.get_day_display(), "state": attendance_info.state})

        return Response(status=status.HTTP_200_OK, data={"attendance_info_list": attendance_info_list})

    def post(self, request):
        week_subject_id = request.data.get('id')
        student = request.user.attendanceuser
        number = int(request.data.get('number'))

        week_subject = WeekSubject.objects.get(id=week_subject_id)
        day_subject = week_subject.find_day_subject()

        if day_subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data="오늘 수업이 없습니다.")

        attendance_number = AttendanceNumber.objects.filter(day_subject=day_subject).order_by(
            '-created_datetime').first()

        if attendance_number:
            today_number = attendance_number.number

            if number == today_number:
                attendance_info = AttendanceInfo.objects.get(student=student, day_subject=day_subject)

                if attendance_info.state != 0:
                    return Response(status=status.HTTP_200_OK, data="이미 처리 되었습니다.")

                # 지각 처리
                # if timezone.now() - timezone.timedelta(minutes=3) > attendance_number.created_datetime:
                #     attendance_info.state = 2

                attendance_info.state = 1
                attendance_info.save()

                return Response(status=status.HTTP_201_CREATED, data={"state": attendance_info.get_state_display()})

            else:
                return Response(status=status.HTTP_404_NOT_FOUND, data="잘못된 번호입니다.")

        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data="발급된 번호가 없습니다.")


class ManageAttendance(APIView):
    serializer_class = AttendanceInfoSerializer

    def get(self, request):
        subject_name = request.GET.get('subject_name')
        professor = request.user.attendanceuser

        week_subjects = WeekSubject.objects.filter(name=subject_name, professor=professor).order_by('week__week_start')

        attendance_info_list = list()

        for week_subject in week_subjects:
            day_subjects = week_subject.day_subjects.order_by('day')

            for day_subject in day_subjects:
                day_attendance_info_list = AttendanceInfo.objects.filter(day_subject=day_subject).order_by(
                    'student__name')

                day_attendance_info_list = [AttendanceInfoSerializer(day_attendance_info).data for day_attendance_info
                                            in day_attendance_info_list]

                attendance_data = {
                    "day": day_subject.get_day_display(),
                    "attendance_info": day_attendance_info_list
                }
                attendance_info_list.append(attendance_data)

        return Response(status=status.HTTP_200_OK, data={"attendance_info_list": attendance_info_list})

    def post(self, request):
        id = request.data.get('id')
        state = request.data.get('state')

        attendance_info = AttendanceInfo.objects.get(id=id)
        attendance_info.state = state
        attendance_info.save()

        data = AttendanceInfoSerializer(attendance_info).data

        return Response(status=status.HTTP_200_OK, data=data)
