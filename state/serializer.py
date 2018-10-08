from rest_framework import serializers
from .models import AttendanceInfo, AttendanceNumber


class AttendanceInfoSerializer(serializers.ModelSerializer):
    # day_subject_list = DaySubjectSerializer(source='day_subjects', read_only=True, many=True)
    student_name = serializers.ReadOnlyField(source='student.name', read_only=True)
    state_display = serializers.SerializerMethodField()

    class Meta:
        model = AttendanceInfo
        fields = ('student_name', 'state', 'id', 'state_display')

    def get_state_display(self, obj):
        return obj.get_state_display()
