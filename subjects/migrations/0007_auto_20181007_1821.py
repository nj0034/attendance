# Generated by Django 2.1.2 on 2018-10-07 09:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('subjects', '0006_auto_20181007_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaySubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, '월'), (1, '화'), (2, '수'), (3, '목'), (4, '금')])),
                ('time', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])),
            ],
        ),
        migrations.CreateModel(
            name='WeekSubject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(max_length=200)),
                ('default', models.BooleanField(default=False)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_professor', to='accounts.AttendanceUser')),
                ('students', models.ManyToManyField(related_name='subject_students', to='accounts.AttendanceUser')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Week')),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='professor',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='students',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='time_info',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='week',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='TimeInfo',
        ),
        migrations.AddField(
            model_name='daysubject',
            name='weekly_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_subject', to='subjects.WeekSubject'),
        ),
    ]