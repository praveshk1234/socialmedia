# Generated by Django 4.1 on 2022-08-18 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_follow_followed_by_alter_follow_followed_to'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('followed_by', 'followed_to')},
        ),
    ]