# Generated by Django 5.0.2 on 2024-06-10 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_likesmodel_post_alter_likesmodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='likes_count',
        ),
    ]
