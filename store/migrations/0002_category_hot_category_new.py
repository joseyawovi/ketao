# Generated by Django 5.1.1 on 2024-09-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='hot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='new',
            field=models.BooleanField(default=False),
        ),
    ]
