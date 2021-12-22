from django.db import models
from django.db.models.fields import BigIntegerField
from phone_field import PhoneField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.urls import reverse
from birthday import BirthdayField, BirthdayManager
from datetime import date


# Create your models here.
class Member(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    STATE = (
        ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi','Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'),('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'),('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo','Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')
    )

    MARITAL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    )

    WING_CHOICE = (
        ('Youth', 'Youth'),
        ('Men', 'Men'),
        ('Women', 'Women'),
    )

    BIRTH_MONTH_CHOICES = zip(range(0, 13), range(0, 13))

    BIRTH_DAY_CHOICES = zip(range(0, 32), range(0, 32))

    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, default='')
    middle_name = models.CharField(max_length=25, blank=True, default='')
    last_name = models.CharField(max_length=25, default='')
    gender = models.CharField(max_length=300, choices=GENDER,)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True, unique=True)
    state_of_origin = models.CharField(max_length=300, blank=True, choices=STATE,)
    address = models.CharField(max_length=300, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=100, blank=True)
    home_cell = models.CharField(max_length=150, default="", blank=True)
    marital_status = models.CharField(max_length=300, choices=MARITAL_STATUS, blank=True)
    occupation = models.CharField(max_length=100, default='', blank=True)
    wing = models.CharField(max_length=25, choices=WING_CHOICE, blank=True,)
    birthday = models.DateField(blank=True, null=True)


    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        names = (self.first_name, self.middle_name, self.last_name)
        return " ".join(names)

    def get_absolute_url(self):
        return reverse('church_app:detail', kwargs={'pk': self.pk})

    # def clean(self):
    #     # Don't allow phone number entries to not begin with zero.
    #     for u in self.phone_number:
    #         if self.phone_number[u] != '0':
    #             raise ValidationError(_('Please enter phone number starting with 0'))
    #     # Dont allow the phone number to be less than or greater than 10.
    #     if self.phone_number != 11:
    #         raise ValidationError(_('Please enter phone number up to 10 digits'))


# try:
#     Member.clean()
# except ValidationError as e:
#     non_field_errors = e.message_dict[NON_FIELD_ERRORS]
