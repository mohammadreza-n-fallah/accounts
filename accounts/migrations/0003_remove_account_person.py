# Generated by Django 5.1.2 on 2024-10-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='person',
        ),
    ]