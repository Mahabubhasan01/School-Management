# Generated by Django 4.0.5 on 2022-07-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_class_manager_model_class_nine_result_model_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentregisterform',
            name='student_class1',
        ),
        migrations.AlterField(
            model_name='studentregisterform',
            name='mother_occupation',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Professor', 'Professor'), ('Businessman', 'Businessman'), ('Sciencist', 'Sciencist'), ('Housewife', 'House-wife'), ('NGO', 'NGO'), ('Banker', 'Banker'), ('Others', 'Others')], default='House-wife', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentregisterform',
            name='student_class',
            field=models.CharField(choices=[('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')], max_length=100),
        ),
    ]
