# Generated by Django 2.1.2 on 2018-10-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0010_auto_20181007_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeksubject',
            name='latitude',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeksubject',
            name='longitude',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
