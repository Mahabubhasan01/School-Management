# Generated by Django 4.0.5 on 2022-07-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenregisterform',
            name='date_of_birth',
            field=models.DateTimeField(max_length=10),
        ),
    ]
