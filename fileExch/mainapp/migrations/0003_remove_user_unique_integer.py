# Generated by Django 4.2.2 on 2023-06-24 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_user_unique_integer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='unique_integer',
        ),
    ]