# Generated by Django 3.1.7 on 2021-03-19 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0011_auto_20210318_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biaoge',
            name='xx',
            field=models.FloatField(help_text='Latitude'),
        ),
        migrations.AlterField(
            model_name='biaoge',
            name='yy',
            field=models.FloatField(help_text='Longtitude'),
        ),
    ]
