# Generated by Django 4.0.5 on 2022-07-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_staffregisterform_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffregisterform',
            name='section',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], default='Morning', max_length=100),
        ),
    ]
