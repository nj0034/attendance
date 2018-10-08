from rest_framework import serializers
from subjects.models import Week, WeekSubject, DaySubject


class WeekSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekSubject
        fields = '__all__'


class DaySubjectSerializer(serializers.ModelSerializer):
    # week_subject = WeekSubjectSerializer(source='week_subject')

    class Meta:
        model = DaySubject
        fields = ('day', 'time')


class WeekSubjectListSerializer(serializers.ModelSerializer):
    day_subject_list = DaySubjectSerializer(source='day_subjects', read_only=True, many=True)

    class Meta:
        model = WeekSubject
        fields = ('id', 'name', 'day_subject_list', 'latitude', 'longitude')
