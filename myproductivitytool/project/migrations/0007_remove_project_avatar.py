# Generated by Django 2.2 on 2019-07-03 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20190702_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='avatar',
        ),
    ]
