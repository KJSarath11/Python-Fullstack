# Generated by Django 5.1.1 on 2024-10-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelapp', '0003_anime'),
    ]

    operations = [
        migrations.CreateModel(
            name='myself',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hobby', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
            ],
        ),
    ]
