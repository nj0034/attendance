# Generated by Django 2.1.2 on 2018-10-07 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0010_auto_20181007_1842'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, choices=[(0, '결석'), (1, '출석'), (2, '지각'), (3, '이탈')], default='', max_length=200)),
                ('day_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.DaySubject')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.AttendanceUser')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('day_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.DaySubject')),
            ],
        ),
    ]
