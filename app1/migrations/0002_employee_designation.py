# Generated by Django 5.2 on 2025-05-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='', max_length=50),
        ),
    ]
