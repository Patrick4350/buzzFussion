# Generated by Django 5.1 on 2024-08-15 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_message_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
