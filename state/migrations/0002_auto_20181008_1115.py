# Generated by Django 2.1.2 on 2018-10-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceinfo',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, '결석'), (1, '출석'), (2, '지각'), (3, '이탈')], default=''),
        ),
    ]