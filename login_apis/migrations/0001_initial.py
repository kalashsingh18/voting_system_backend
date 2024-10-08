# Generated by Django 5.1.1 on 2024-09-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1234)),
                ('email', models.EmailField(default='default_email@example.com', max_length=254)),
                ('password', models.TextField(max_length=13456)),
            ],
        ),
    ]
