# Generated by Django 2.0.6 on 2020-07-08 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='stripe_account',
        ),
    ]
