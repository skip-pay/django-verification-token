# Generated by Django 2.2.15 on 2020-11-12 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verification_token', '0004_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verificationtoken',
            name='expiration_in_minutes',
        ),
    ]
