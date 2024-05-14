# Generated by Django 5.0.3 on 2024-04-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_employee_department_remove_employee_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Role', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
