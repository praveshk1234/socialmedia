# Generated by Django 4.1 on 2022-08-18 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_profile_followers_delete_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='app.profile')),
                ('followed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_to', to='app.profile')),
            ],
        ),
    ]
