# Generated by Django 2.1.2 on 2018-10-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_auto_20181007_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeinfo',
            name='day',
            field=models.CharField(choices=[(0, '월'), (1, '화'), (2, '수'), (3, '목'), (4, '금')], max_length=200),
        ),
    ]
