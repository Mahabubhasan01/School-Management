# Generated by Django 4.0.5 on 2022-07-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Eight_Result_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Manager_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('section_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Nine_Result_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Seven_Result_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Six_Result_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Ssc_Result_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Ten_Result_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Result_Model_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StaffRegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('subject_choice', models.CharField(choices=[('Bangla', 'Bangla'), ('English', 'English'), ('Math', 'Math'), ('ICT', 'ICT'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Higher Math', 'Higher Math'), ('Accounting', 'Accounting'), (
                    'Finance & Banking', 'Finance & Banking'), ('General Science', 'General Science'), ('Bussiness Studies', 'Bussiness Studies'), ('Economics', 'Economics'), ('History', 'History'), ('Ethics', 'Ethics'), ('Others', 'Others')], default='Chemistry', max_length=100)),
                ('date_of_birth', models.DateTimeField(max_length=10)),
                ('gender', models.CharField(choices=[
                 ('male', 'male'), ('female', 'female')], default='male', max_length=20)),
                ('course', models.CharField(choices=[('Science', 'Science'), ('Commerce', 'Commerce'), (
                    'Arts', 'Arts'), ('Others', 'Others')], default='Science', max_length=100)),
                ('section', models.CharField(choices=[('Morning', 'Morning'), (
                    'Afternoon', 'Afternoon'), ('Evening', 'Evening')], default='Morning', max_length=100)),
                ('phone_number', models.IntegerField()),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), (
                    'AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('Others', 'Others')], default='A+', max_length=10)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Christan', 'Chirstan'), (
                    'Hindu', 'Hindu'), ('Buddho', 'Buddho'), ('Others', 'Others')], default='Islam', max_length=50)),
                ('profile_img', models.ImageField(null=True, upload_to='assets')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_name', models.CharField(choices=[
                 ('First-Terms', 'First-Terms'), ('Second-Terms', 'Second-Terms'), ('Final-Terms', 'Final-Terms')], max_length=100)),
                ('class_name', models.CharField(choices=[('Six', 'Six'), ('Seven', 'Seven'), (
                    'Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')], max_length=100)),
                ('section_name', models.CharField(choices=[('Rose', 'Rose'), ('Lotus', 'Lotus'), ('Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), (
                    'Tulip', 'Tulip'), ('Science', 'Science'), ('Commerce', 'Commerce'), ('Jasmine', 'Arts')], default='Jasmine', max_length=100)),
                ('start_date', models.DateTimeField(max_length=100)),
                ('end_date', models.DateTimeField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_name', models.CharField(choices=[
                 ('First-Terms', 'First-Terms'), ('Second-Terms', 'Second-Terms'), ('Final-Terms', 'Final-Terms')], max_length=100)),
                ('class_name', models.CharField(choices=[('Six', 'Six'), ('Seven', 'Seven'), (
                    'Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')], max_length=100)),
                ('section_name', models.CharField(choices=[('Rose', 'Rose'), ('Lotus', 'Lotus'), ('Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), (
                    'Tulip', 'Tulip'), ('Science', 'Science'), ('Commerce', 'Commerce'), ('Jasmine', 'Arts')], default='Jasmine', max_length=100)),
                ('published_date', models.DateTimeField(max_length=100)),
                ('attached_file', models.FileField(upload_to='assets')),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('admission_roll', models.IntegerField(default=101)),
                ('email_address', models.EmailField(
                    default='Mahabubhasaan@outlook.com', max_length=200)),
                ('student_class', models.CharField(choices=[('Six', 'Six'), ('Seven', 'Seven'), (
                    'Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')], max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(choices=[('Teacher', 'Teacher'), ('Professor', 'Professor'), ('Businessman', 'Businessman'), (
                    'Sciencist', 'Sciencist'), ('Farmer', 'Farmer'), ('NGO', 'NGO'), ('Banker', 'Banker'), ('Others', 'Others')], default='Teacher', max_length=100)),
                ('mother_occupation', models.CharField(choices=[('Teacher', 'Teacher'), ('Professor', 'Professor'), ('Businessman', 'Businessman'), (
                    'Sciencist', 'Sciencist'), ('Housewife', 'House-wife'), ('NGO', 'NGO'), ('Banker', 'Banker'), ('Others', 'Others')], default='House-wife', max_length=100)),
                ('date_of_birth', models.DateTimeField(max_length=10)),
                ('gender', models.CharField(choices=[
                 ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('course', models.CharField(max_length=100)),
                ('section', models.CharField(choices=[('Rose', 'Rose'), ('Lotus', 'Lotus'), ('Jasmine', 'Jasmine'), (
                    'Orchid', 'Orchid'), ('Tulip', 'Tulip')], default='Jasmine', max_length=100)),
                ('phone_number', models.IntegerField()),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), (
                    'AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('Others', 'Others')], default='A+', max_length=10)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Christan', 'Chirstan'), (
                    'Hindu', 'Hindu'), ('Buddho', 'Buddho'), ('Others', 'Others')], default='Islam', max_length=50)),
                ('address', models.TextField(
                    default='House No. 290, Mirpur Section - 12 Dhaka - 1000 ,Bangladesh', max_length=500)),
                ('profile_img', models.ImageField(null=True, upload_to='assets')),
            ],
        ),
        migrations.CreateModel(
            name='Subject_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
                ('teacher_name', models.CharField(max_length=100)),
            ],
        ),
    ]
