# Generated by Django 5.0.3 on 2024-04-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_guardian_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian_details',
            name='Name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='Name',
            field=models.CharField(max_length=30),
        ),
    ]
