from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    DEPARTMENTS = (
        ('', 'Select'),
        ('Music Production', 'Music Production'),
        ('Software Development', 'Software Development'),
        ('Computer Gaming', 'Computer Gaming'),
    )
    department = models.CharField(max_length=100, null=True, blank=True, choices=DEPARTMENTS)
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=16, choices=GENDERS, null=True, default=None)
    address = models.TextField(null=True, blank=True)
    LANGUAGES = (
        ('English', 'English'),
        ('Bangla', 'Bangla'),
        ('Hindi', 'Hindi'),
    )
    language = MultiSelectField(max_length=128, null=True, blank=True, choices=LANGUAGES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name