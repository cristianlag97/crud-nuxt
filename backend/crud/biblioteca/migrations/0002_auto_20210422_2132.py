# Generated by Django 3.1.7 on 2021-04-23 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='anno_fallece',
            field=models.DateField(blank=True, null=True),
        ),
    ]
