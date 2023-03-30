from django.db import models
from django.conf import settings
from django.contrib import admin
from services.hospital.models import HospitalModel, HospitalStaff, StaffDepartment

# from rest_framework.decorators import display


# Create your models here.



class PatientModel(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Other'),
    ]

    BLOOD_GROUP_A_POSITIVE = 'A+'
    BLOOD_GROUP_A_NEGATIVE = 'A-'
    BLOOD_GROUP_B_POSITIVE = 'B+'
    BLOOD_GROUP_B_NEGATIVE = 'B-'
    BLOOD_GROUP_O_POSITIVE = 'O+'
    BLOOD_GROUP_O_NEGATIVE = 'O-'
    BLOOD_GROUP_AB_POSITIVE = 'AB+'
    BLOOD_GROUP_AB_NEGATIVE = 'AB-'

    BLOOD_GROUP_CHOICES = [
        (BLOOD_GROUP_A_POSITIVE, 'A+'),
        (BLOOD_GROUP_A_NEGATIVE, 'A-'),
        (BLOOD_GROUP_B_POSITIVE, 'B+'),
        (BLOOD_GROUP_B_NEGATIVE, 'B-'),
        (BLOOD_GROUP_O_POSITIVE, 'O+'),
        (BLOOD_GROUP_O_NEGATIVE, 'O-'),
        (BLOOD_GROUP_AB_NEGATIVE, 'AB+'),
        (BLOOD_GROUP_AB_NEGATIVE, 'AB-'),
    ]

    GENOTYPE_AA = 'AA'
    GENOTYPE_AS = 'AS'
    GENOTYPE_AC = 'AC'
    GENOTYPE_SS = 'SS'
    GENOTYPE_SC = 'SC'

    GENOTYPE_CHOICES = [
        (GENOTYPE_AA, 'AA'),
        (GENOTYPE_AS, 'AS'),
        (GENOTYPE_AC, 'AC'),
        (GENOTYPE_SS, 'SS'),
        (GENOTYPE_SC, 'SC'),
    ]

    
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=False)
    address = models.CharField(max_length=250, null=False)
    blood_group = models.CharField(max_length=6, choices=BLOOD_GROUP_CHOICES, blank=True, null=False)
    genotype = models.CharField(max_length=11, choices=GENOTYPE_CHOICES, blank=True, null=False)
    phone = models.CharField(max_length=14, null=False, blank=False, unique=True)
    medical_history = models.ImageField(upload_to='profile_image', null=False, blank=False, default='blank_profile_pic.png')
    profile_picture = models.ImageField(upload_to='profile_image', blank=False, default='blank_profile_pic.png')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]

class MedicalPersonnel(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Other'),
    ]

    SPECIALTY_CHOICES = (

     ('epidemiologist', 'Epidemiologist'),
        ('general practitioner', 'General practitioner'),
        ('pediatrician', 'Pediatrician'),
        ('dentist', 'Dentist'),

        ('surgeon', 'Surgeon'),
        ('dermatologist', 'Dermatologist'),
        ('plastic surgeon', ' Plastic Surgeon'),
        ('psychiatrist', 'Psychiatrist'),
    )

    
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False)
    hospital_staff_id = models.CharField(max_length=25, blank= False, unique=True)
    profile_picture = models.ImageField(upload_to='profile_image', blank=False, default='blank_profile_pic.png')
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES)
    # hospital = models.CharField(max_length=20, blank=False)
    medical_profession = models.CharField(max_length=30, blank=True)
    # speciality = models.ForeignKey(StaffDepartment, on_delete=models.CASCADE, related_name='department')
    hospital = models.ForeignKey(HospitalModel, on_delete=models.CASCADE, related_name='hopsital_name')
    # clinical_profession = models.ForeignKey(HospitalStaff, on_delete=models.CASCADE, related_name='job')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.user.first_name} {self.medical_profession} {self.user.last_name}\
        {self.hospital.name} {self.hospital.address} {self.specialty}'

    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    # @admin.display(ordering='profession__staffs')
    # def profession(self):
    #     return self.clinical_profession.staffs

    @admin.display(ordering='hospital__name')
    def hospital_name(self):
        return self.hospital.name


    # @admin.display(ordering='hospital__address')
    # def hospital_address(self):
    #     return self.user.last_name

    class Meta:
        ordering = ['hospital__name', 'user__first_name', 'user__last_name', 'profile_picture']
        permissions = [
            ('view_history', 'Can view history')
        ]










