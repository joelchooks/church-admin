from operator import mod
from shutil import _ntuple_diskusage
from django.db import models
from django.db.models.fields import BigIntegerField
from phone_field import PhoneField
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.urls import reverse, reverse_lazy
from birthday import BirthdayField, BirthdayManager
from datetime import date, timezone, datetime
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator





# Create your models here.

# Home Cell
class HomeCell(models.Model):
     
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    cell_name = models.CharField(max_length=300,)
    cell_leader = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='homecell_rel', default='',)
    cell_address = models.CharField(max_length=300,)
    date_added = models.DateTimeField(default=datetime.now, editable=False)
    last_updated = models.DateTimeField(editable=True, default=datetime.now)
    is_active = models.BooleanField(default=True, choices=TRUE_FALSE_CHOICES)

    
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.cell_name

    def get_absolute_url(self):
        return reverse('home_cell:cell_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.last_updated = datetime.now()
        super(HomeCell, self).save(*args, **kwargs)
    
    @property
    def membersis(self):
        print(self.member_rel.all())
        return self.member_rel.all()

# Member Model
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
        # ('Divorced', 'Divorced'),
    )

    WING_CHOICE = (
        ('Youth', 'Youth'),
        ('Men', 'Men'),
        ('Women', 'Women'),
    )

    DEPARTMENT_CHOICES = (
        ('Media', 'Media'),
        ('Choir', 'Choir'),
        ('Sanctuary', 'Sanctuary')
    )

    MEMBER_CHOICES = (
        ('Member', 'Member'),
        ('New Member', 'New Member'),
        ('Guest', 'Guest'),
        ('Former Member', 'Former Member')
    )

    # BIRTH_MONTH_CHOICES = zip(range(0, 13), range(0, 13))
    # BIRTH_DAY_CHOICES = zip(range(0, 32), range(0, 32))

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    BAPTISM_TRUE_FALSE_CHOICES = (
        (True, 'Baptized'),
        (False, 'Not Yet')
    )

    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25,)
    middle_name = models.CharField(max_length=25, blank=True, default='',)
    last_name = models.CharField(max_length=25,)
    gender = models.CharField(max_length=300, choices=GENDER,)
    phone_number = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex=r'^\d{11,11}$', message='Value Must Be Numeric And Up To 11 Digits',
            code='invalid_number')])    
    other_number = models.CharField(max_length=11, unique=True, blank=True, null=True, validators=[RegexValidator(regex=r'^\d{11,11}$', message='Value Must Be Numeric And Up To 11 Digits',
            code='invalid_number')])
    email = models.EmailField(blank=True, null=True, unique=True)
    state_of_origin = models.CharField(max_length=300, blank=True, choices=STATE,)
    address = models.CharField(max_length=300, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(editable=False)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default='Media', blank=True)
    home_cell = models.ForeignKey(HomeCell, on_delete=models.CASCADE, related_name='member_rel', default='', blank=True, null=True)
    marital_status = models.CharField(max_length=300, choices=MARITAL_STATUS, blank=True)
    occupation = models.CharField(max_length=100, default='', blank=True)
    wing = models.CharField(max_length=25, choices=WING_CHOICE, blank=True,)
    birthday = models.DateField(default=datetime.now, blank=True, null=True)
    # Remove Is Member
    is_member = models.BooleanField(default=False, blank=True, null=True)
    member_status = models.CharField(default='Member', choices=MEMBER_CHOICES, max_length=25, blank=True, null=True)
    member_age = models.PositiveIntegerField(null=True, blank=True, editable=False)
    is_baptized = models.BooleanField(default=True, choices=BAPTISM_TRUE_FALSE_CHOICES, blank=True, null=True)
    done_foundation = models.BooleanField(default=True, choices=TRUE_FALSE_CHOICES, blank=True, null=True)
    done_maturity = models.BooleanField(default=False, choices=TRUE_FALSE_CHOICES, blank=True, null=True)


    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        names = (self.first_name, self.middle_name, self.last_name)
        return " ".join(names)

    def get_absolute_url(self):
        return reverse('church_app:detail', kwargs={'pk': self.pk})
    
    
    def save(self, *args, **kwargs):
        if self.birthday != None:
            today = date.today()
            self.member_age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))  
        ''' On save, update timestamps '''
        self.last_updated = datetime.now()
        self.first_name = self.first_name.title()
        self.middle_name = self.middle_name.title()
        self.last_name = self.last_name.title()
        
        super(Member, self).save(*args, **kwargs)



# Attendance
class MemberAttendance(models.Model):
    
    service_type_choices = (
        ('Sunday Service', 'Sunday Service'),
        ('Tueday Healing & Deliverance', 'Tuesday Healing & Deliverance'),
        ('Wednesday Mid-Week Service', 'Wednesday Mid-Week Service'),
        ('Friday Worship & Wonders Night', 'Friday Worship & Wonders Night'),
        ('Others', 'Others')
    )


    date = models.DateField(default=datetime.now)
    service_Type = models.CharField(max_length=70, choices=service_type_choices, default='Sunday Service')
    overall_total = models.PositiveBigIntegerField(default=0, blank=True)
    
    def get_absolute_url(self):
        if self.pk:
            return reverse_lazy('church_app:att_detail', kwargs={'pk':self.pk,})
        return reverse_lazy('church_app:att_list')

    def __str__(self):
        return f'{self.service_Type}'

    
    class Meta:
        ordering = ['-date']

    # def save(self, *args, **kwargs):
    #     self.overall_total = sum(newTot)
    #     print(self.overall_total)
       
    #     super(MemberAttendance, self).save(*args, **kwargs)
    
    


class Service(models.Model):
    service = models.ForeignKey(MemberAttendance, on_delete=models.CASCADE)
    no_of_men = models.PositiveIntegerField(default=0, blank=True)
    no_of_women = models.PositiveIntegerField(default=0, blank=True)
    no_of_children = models.PositiveIntegerField(default=0, blank=True)
    no_of_new_comers = models.PositiveIntegerField(default= 0, blank=True)
    no_of_new_converts = models.PositiveIntegerField(default=0, blank=True)
    total = models.PositiveIntegerField(default=0, blank=True)
    
    def __str__(self):
        return f'{self.total}'

    def save(self, *args, **kwargs):
        
        self.total = self.no_of_men + self.no_of_women + self.no_of_children
        super(Service, self).save(*args, **kwargs)
        # super(MemberAttendance, self).save(*args, **kwargs)
       

       

class Message(models.Model):

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    sender_name = models.CharField(max_length=12)
    recipients = models.TextField(max_length=50000000000)
    message_text = models.TextField(max_length=919)
    flash = models.BooleanField(default=False, choices = TRUE_FALSE_CHOICES)
    created_date = models.DateTimeField(default=datetime.now)
    approved_message = models.BooleanField(default=False)
    sent_date = models.DateTimeField(blank=True, null=True)


    def approve(self):
        self.approved_message = True
        self.sent_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('church_app:message_draft')

    def save(self, *args, **kwargs):
        if self.approved_message:
            self.sent_date = datetime.now()
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.created_date}'




    # def __str__(self):
    #     return self.day


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
