from django.db import models
from member_app.models import Member

# Create your models here.
class HomeCellMembers(models.Model):
    cell_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='allcellmembers_set')
    address = models.CharField(verbose_name='Address', max_length=100, null=True, blank=True)
    town = models.CharField(verbose_name='Town/City', max_length=100, null=True, blank=True)
    county = models.CharField(verbose_name='County', max_length=100, null=True, blank=True)
    post_code = models.CharField(verbose_name='Post Code', max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name='Country', max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name='Longitude', max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name='Latitude', max_length=50, null=True, blank=True)

    has_cell = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cell_member
