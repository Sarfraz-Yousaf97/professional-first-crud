# Generated by Django 3.2.9 on 2022-08-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('author_profile', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('overview', models.CharField(max_length=500)),
            ],
        ),
    ]