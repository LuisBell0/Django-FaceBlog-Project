# Generated by Django 5.0.2 on 2024-05-02 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_date',
            field=models.DateField(blank=True, default=datetime.date(2024, 5, 2), null=True),
        ),
    ]