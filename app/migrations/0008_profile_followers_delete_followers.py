# Generated by Django 4.1 on 2022-08-18 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_followers_another_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followuser', to='app.profile'),
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
    ]