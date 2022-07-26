from email.policy import default
from django.db import models
from django.urls import reverse
# Create your models here.


# Staff Register Form

class StaffRegisterForm(models.Model):
    father_choice = (("Teacher", "Teacher"), ("Professor", "Professor"),
                     ("Businessman", "Businessman"), ("Sciencist", "Sciencist"), ("Farmer", "Farmer"), ("NGO", "NGO"), ("Banker", "Banker"), ('Others', 'Others'),)

    mother_choice = (("Teacher", "Teacher"), ("Professor", "Professor"),
                     ("Businessman", "Businessman"), ("Sciencist", "Sciencist"), ("Housewife", "House-wife"), ("NGO", "NGO"), ("Banker", "Banker"), ('Others', 'Others'),)

    blood_group = (('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+',
                   'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('Others', 'Others'),)

    religion_group = (('Islam', 'Islam'), ('Christan', 'Chirstan'),
                      ('Hindu', 'Hindu'), ('Buddho', 'Buddho'), ('Others', 'Others'),)

    student_name = models.CharField(max_length=100, default='kochu')
    admission_roll = models.IntegerField(default=101)
    email_address = models.EmailField(
        max_length=200, default='Mahabubhasaan@outlook.com')
    student_class = models.CharField(max_length=100, choices=(
        ('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten'),),)
    section = models.CharField(max_length=100, choices=(('Rose', 'Rose'), ('Lotus', 'Lotus'), (
        'Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), ('Tulip', 'Tulip'), ('Science', 'Science'), ('Commerce', 'Commerce'), (
        'Jasmine', 'Arts'),), default='Jasmine')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_occupation = models.CharField(
        max_length=100, choices=father_choice, default='Teacher')
    mother_occupation = models.CharField(
        max_length=100, choices=mother_choice, default='House-wife')
    date_of_birth = models.DateTimeField(max_length=10)
    gender = models.CharField(max_length=20, choices=(
        ("Male", "Male"), ("Female", "Female")), default='Male')
    course = models.CharField(max_length=100)
    section = models.CharField(max_length=100, choices=(('Rose', 'Rose'), ('Lotus', 'Lotus'), (
        'Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), ('Tulip', 'Tulip'),), default='Jasmine')
    phone_number = models.IntegerField()
    blood_group = models.CharField(
        max_length=10, choices=blood_group, default='A+')
    religion = models.CharField(
        max_length=50, choices=religion_group, default='Islam')
    address = models.TextField(
        max_length=500, default='House No. 290, Mirpur Section - 12 Dhaka - 1000 ,Bangladesh')
    profile_image = models.ImageField(
        upload_to='assets', null=True, default='"https://bootdey.com/img/Content/avatar/avatar3.png"')

    def __str__(self):
        return self.student_name


# Student Register Form

class StudentRegisterForm(models.Model):
    father_choice = (("Teacher", "Teacher"), ("Professor", "Professor"),
                     ("Businessman", "Businessman"), ("Sciencist", "Sciencist"), ("Farmer", "Farmer"), ("NGO", "NGO"), ("Banker", "Banker"), ('Others', 'Others'),)

    mother_choice = (("Teacher", "Teacher"), ("Professor", "Professor"),
                     ("Businessman", "Businessman"), ("Sciencist", "Sciencist"), ("Housewife", "House-wife"), ("NGO", "NGO"), ("Banker", "Banker"), ('Others', 'Others'),)

    blood_group = (('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+',
                   'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('Others', 'Others'),)

    religion_group = (('Islam', 'Islam'), ('Christan', 'Chirstan'),
                      ('Hindu', 'Hindu'), ('Buddho', 'Buddho'), ('Others', 'Others'),)

    student_name = models.CharField(max_length=100)
    admission_roll = models.IntegerField(default=101)
    email_address = models.EmailField(
        max_length=200, default='Mahabubhasaan@outlook.com')
    student_class = models.CharField(max_length=100, choices=(
        ('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten'),),)
    section = models.CharField(max_length=100, choices=(('Rose', 'Rose'), ('Lotus', 'Lotus'), (
        'Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), ('Tulip', 'Tulip'), ('Science', 'Science'), ('Commerce', 'Commerce'), (
        'Jasmine', 'Arts'),), default='Jasmine')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_occupation = models.CharField(
        max_length=100, choices=father_choice, default='Teacher')
    mother_occupation = models.CharField(
        max_length=100, choices=mother_choice, default='House-wife')
    date_of_birth = models.DateTimeField(max_length=10)
    gender = models.CharField(max_length=20, choices=(
        ("Male", "Male"), ("Female", "Female")), default='Male')
    course = models.CharField(max_length=100)
    section = models.CharField(max_length=100, choices=(('Rose', 'Rose'), ('Lotus', 'Lotus'), (
        'Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), ('Tulip', 'Tulip'),), default='Jasmine')
    phone_number = models.IntegerField()
    blood_group = models.CharField(
        max_length=10, choices=blood_group, default='A+')
    religion = models.CharField(
        max_length=50, choices=religion_group, default='Islam')
    address = models.TextField(
        max_length=500, default='House No. 290, Mirpur Section - 12 Dhaka - 1000 ,Bangladesh')
    profile_image = models.ImageField(upload_to='assets', null=True,)

    def __str__(self):
        return self.student_name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self) -> str:
        return self.title


class Subject_Manager(models.Model):
    subject_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)


class Class_Manager_Model(models.Model):
    teacher_name = models.CharField(
        max_length=50, default='Aolad Hossian Sorkar')
    subject_name = models.CharField(max_length=100, choices=(('Bangla', 'Bangla'), ('English', 'English'), (
        'Math', 'Math'), ('Ict', 'Ict'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), (
        'Higher Math', 'Higher Math'), ('Accounting', 'Accounting'), ('Finance Banking', 'Finance Banking'), ('Business Studies', 'Business Studies'), ('Ethics', 'Ethics'), ('History', 'History'), ('Physical Education', 'Physical Education'), ('Agriculture Studies', 'Agriculture Studies'), ('Computer Studies', 'Computer Studies'),), default='Physics')
    class_name = models.CharField(max_length=100, choices=(
        ('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten'),),)
    class_serial = models.CharField(max_length=100, choices=(
        ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th'),), default='1st')
    section_name = models.CharField(max_length=100, choices=(('Rose', 'Rose'), ('Lotus', 'Lotus'), (
        'Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), ('Tulip', 'Tulip'), ('Science', 'Science'), ('Commerce', 'Commerce'), (
        'Arts', 'Arts'),), default='Jasmine')


class Student_Exam(models.Model):
    terms_name = models.CharField(max_length=100, choices=(
        ('First-Terms', 'First-Terms'), ('Second-Terms', 'Second-Terms'), ('Final-Terms', 'Final-Terms'),),)
    class_name = models.CharField(max_length=100, choices=(
        ('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten'),),)
    section_name = models.CharField(max_length=100, choices=(('Rose', 'Rose'), ('Lotus', 'Lotus'), (
        'Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), ('Tulip', 'Tulip'), ('Science', 'Science'), ('Commerce', 'Commerce'), (
        'Jasmine', 'Arts'),), default='Jasmine')
    start_date = models.DateTimeField(max_length=100)
    end_date = models.DateTimeField(max_length=100)


class Student_Result(models.Model):
    terms_name = models.CharField(max_length=100, choices=(
        ('First-Terms', 'First-Terms'), ('Second-Terms', 'Second-Terms'), ('Final-Terms', 'Final-Terms'),),)
    class_name = models.CharField(max_length=100, choices=(
        ('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten'),),)
    section_name = models.CharField(max_length=100, choices=(('Rose', 'Rose'), ('Lotus', 'Lotus'), (
        'Jasmine', 'Jasmine'), ('Orchid', 'Orchid'), ('Tulip', 'Tulip'), ('Science', 'Science'), ('Commerce', 'Commerce'), (
        'Jasmine', 'Arts'),), default='Jasmine')
    published_date = models.DateTimeField(max_length=100)
    attached_file = models.FileField(upload_to='assets')
