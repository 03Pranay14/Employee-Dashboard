# Generated by Django 5.0.3 on 2024-04-25 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_rename_address_contact_address_of_contact_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contact_details',
        ),
    ]
