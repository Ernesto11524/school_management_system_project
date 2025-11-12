''''
This is the models.py file for the user_profile app.
It sets up the database for the users of the application.
It include the following models;
CustomUser : A custom user model which includes additional data of users.
Student : A model which handles information about students in the school.
Teacher : A model which handles information about teachers in the school.
Both the student and teacher models are connected to the user model using OneToOneField
because each user can either be a student or teacher, otherwise the admin.
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

# This model is going to serve as the auth user model of the project. 
# It inherits from the built-in AbstractUser which gives all the built-in django user fields to 
# the customuser model but allow us to add additional fields to it all well.

class CustomUser(AbstractUser):
    # This handles the choices of the roles of the user.
    ROLE_CHOICES = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin'),
    )

    # This handles the choices of the gender of the user.
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    username = models.CharField(max_length=30, null=False, blank=True, unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES) # This field identifies the role of the user in the school.
    profile_picture = models.ImageField() # This field allow us add a picture to the user's profile for easy identification.
    date_of_birth = models.DateField(null=True) # This field is reposible for the user's date of birth.
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES) # This field is responsible for the user's gender.
    phone_number = models.CharField(max_length=15) # This field handles the contact info of the user.
    emergency_contact = models.CharField(max_length=15) # This field takes in the contact of the person to call incase of an emergency.
    address = models.CharField(max_length=50) # This fields adds the address of the user to the user's information.

# This is a student model which include additional fields for the necessary information about a student user.
# It is connected to the customuser model through a onetoonefield relationship. Meaning, an instance of a customuser
# can only be connected to one instance of the student model.
# This prevent users from being connected to more than one instance of the student model.
class Student(models.Model):
    # This tuple of choices is created to specify the relation the guardian has with the student.
    GUARDIAN_RELATION_CHOICES = (
        ('Parent', 'Parent'),
        ('Sibling', 'Sibling'),
        ('Other', 'Other'),
    )

    # This tuple of choices is to assign a class to a student when registered in the school.
    CLASS_CHOICES = (
        ('Creche', 'Creche'),
        ('Nursery', 'Nursery'),
        ('KG1', 'KG1'),
        ('KG2', 'KG2'),
        ('Primary 1', 'Primary 1'),
        ('Primary 2', 'Primary 2'),
        ('Primary 3', 'Primary 3'),
        ('Primary 4', 'Primary 4'),
        ('Primary 5', 'Primary 5'),
        ('Primary 6', 'Primary 6'),
        ('JHS 1', 'JHS 1'),
        ('JHS 2', 'JHS 2'),
        ('JHS 3', 'JHS 3'),
    )

    # This field connects the student model to the custom user model through a onetoone relationship. Each student is supposed to be a user first.
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student')
    guardian_name = models.CharField(max_length=100) # This field takes in the name of the student guardian's name.
    guardian_relation = models.CharField(max_length=30, choices=GUARDIAN_RELATION_CHOICES) # This field specifies the relationship between the student and the guardian.
    guardian_contact = models.CharField(max_length=15) # This field is responsible for the student guardian's contact.
    class_assigned = models.CharField(max_length=30, choices=CLASS_CHOICES)

# This model is responsible for the additional information for teachers registered in the school.
# This teacher is connected to the custom user model through a onetoonefield relationship meaning only.
# one instance of the user model can be connected to an instance of the teacher model.
# This prevent users from being connected to more than one teacher instance.
class Teacher(models.Model):
    # This field connects the teacher model.to the user_model.
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher')
