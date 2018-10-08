from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import AttendanceUser
from .models import Week, WeekSubject, DaySubject
from .serializer import WeekSubjectSerializer, WeekSubjectListSerializer, DaySubjectSerializer


class SubjectManagement(APIView):
    serializer_class = WeekSubjectSerializer

    def get(self, request):
        id = request.GET.get('id')
        subject = get_object_or_404(WeekSubject, pk=id)
        serializer = WeekSubjectSerializer(subject)

        return Response(status=status.HTTP_200_OK, data={"subject": serializer.data})

    def post(self, request):
        professor = request.user.attendanceuser

        week = Week.find_week()
        name = request.data.get('name')
        time_info = request.data.get('time_info')
        default = request.data.get('default', False)
        student_list = request.data.get('student_list', list())

        week_subject_result = WeekSubject.objects.get_or_create(professor=professor, week=week, name=name, default=default)
        week_subject = week_subject_result[0]
        created = week_subject_result[1]

        if created:
            # week_subject.default = True
            # week_subject.save()
            week_subject.set_students(student_list)

        DaySubject.objects.get_or_create(week_subject=week_subject, **time_info)
        # day_subject = day_subject_result[0]
        # created = day_subject_result[1]
        #
        # if created:

        serializer = WeekSubjectSerializer(week_subject)

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    # def patch(self, request):
    #     id = request.data.get('id')
    #     subject = get_object_or_404(Subject, pk=id)
    #     time_info_list = request.data.get('time_info_list')
    #
    #     subject.set_time_info(time_info_list)
    #
    #     return Response(status=status.HTTP_200_OK, data=time_info_list)

    # def delete(self):


class ProfessorSubjectList(ListAPIView):
    queryset = WeekSubject.objects.all()
    serializer_class = WeekSubjectListSerializer

    def get_queryset(self):
        professor = self.request.user.attendanceuser
        subjects = WeekSubject.objects.filter(professor=professor, week=Week.find_week())

        return subjects


class StudentSubjectList(ListAPIView):
    serializer_class = WeekSubjectListSerializer

    def get_queryset(self):
        student = self.request.user.attendanceuser
        subjects = WeekSubject.objects.filter(students=student, week=Week.find_week())

        return subjects


class WeekInfo(APIView):
    def get(self, request):
        week = Week.find_week()
        data = {"week_start": week.week_start, "week_end": week.week_end}

        return Response(status=status.HTTP_200_OK, data=data)
