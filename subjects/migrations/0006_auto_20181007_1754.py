# Generated by Django 2.1.2 on 2018-10-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0005_auto_20181007_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeinfo',
            name='day',
            field=models.IntegerField(choices=[(0, '월'), (1, '화'), (2, '수'), (3, '목'), (4, '금')]),
        ),
    ]
