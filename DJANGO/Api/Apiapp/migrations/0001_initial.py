# Generated by Django 5.1.1 on 2024-10-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bus_no', models.IntegerField()),
                ('start_point', models.CharField(max_length=100)),
                ('end_point', models.CharField(max_length=100)),
            ],
        ),
    ]
