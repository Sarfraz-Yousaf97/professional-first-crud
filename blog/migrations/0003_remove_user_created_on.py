# Generated by Django 3.2.9 on 2022-08-03 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220803_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_on',
        ),
    ]
