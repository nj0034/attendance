# Generated by Django 2.1.2 on 2018-10-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0002_auto_20181008_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceinfo',
            name='state',
            field=models.IntegerField(choices=[(1, '출석'), (2, '지각'), (3, '이탈'), (4, '결석')], default=0),
        ),
    ]