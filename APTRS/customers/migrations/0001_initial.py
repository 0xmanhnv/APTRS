# Generated by Django 4.2.15 on 2024-11-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('img', models.ImageField(upload_to='company')),
                ('address', models.TextField()),
                ('internal', models.BooleanField(default=False)),
            ],
        ),
    ]
