# Generated by Django 4.1 on 2022-08-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_follow_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='no_of_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to='app.profile'),
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
    ]
