# Generated by Django 4.1.7 on 2023-03-23 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
    ]
