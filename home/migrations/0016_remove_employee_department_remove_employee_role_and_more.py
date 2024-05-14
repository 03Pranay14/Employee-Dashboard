# Generated by Django 5.0.3 on 2024-04-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_employee_department_alter_employee_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Role',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='hire_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=None, max_length=200),
        ),
    ]