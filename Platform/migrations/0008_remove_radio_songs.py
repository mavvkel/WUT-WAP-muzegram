# Generated by Django 4.1.5 on 2023-01-23 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Platform', '0007_alter_radio_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radio',
            name='songs',
        ),
    ]
