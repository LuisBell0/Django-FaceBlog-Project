# Generated by Django 5.0.2 on 2024-06-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_comment_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]