# Generated by Django 2.2 on 2019-07-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20190702_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('A', 'Low'), ('B', 'Medium'), ('C', 'High')], default='A', max_length=2),
        ),
    ]
