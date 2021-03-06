# Generated by Django 2.1.2 on 2018-10-06 10:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(max_length=200)),
                ('default', models.BooleanField(default=False)),
                ('professor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subject_professor', to='accounts.AttendanceUser')),
                ('students', models.ManyToManyField(related_name='subject_students', to='accounts.AttendanceUser')),
            ],
        ),
        migrations.CreateModel(
            name='TimeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', '월'), ('Tuesday', '화'), ('Wednesday', '수'), ('Thursday', '목'), ('Friday', '금')], max_length=200)),
                ('time', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start', models.DateField(verbose_name='한 주 시작 날짜')),
                ('week_end', models.DateField(verbose_name='한 주 종료 날짜')),
            ],
            options={
                'verbose_name': '주간',
                'verbose_name_plural': '주간',
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='time_info',
            field=models.ManyToManyField(to='subjects.TimeInfo'),
        ),
        migrations.AddField(
            model_name='subject',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Week'),
        ),
    ]
