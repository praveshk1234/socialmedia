# Generated by Django 4.1 on 2022-08-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_post_no_of_likes_post_likes_delete_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to='app.profile'),
        ),
    ]
