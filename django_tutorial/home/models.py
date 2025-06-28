from django.db import models
SEATING_CHOICES = [
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    ]
# Create your models here.
class menu(models.Model):
    item_name = models.CharField(max_length=100)
    item_decs = models.TextField()

class deals(models.Model):
    food_name = models.CharField(max_length=100)
    food_desc = models.CharField(max_length=255)
    food_image = models.ImageField(upload_to='deals')

class booking(models.Model):
    c_name = models.CharField(max_length=255)
    c_phone = models.CharField(max_length=10)
    c_email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    no_guest = models.CharField(max_length=255)
    seating_pref = models.CharField(max_length=255, choices=SEATING_CHOICES, blank=True, null=True)
    sp_request = models.CharField(max_length=255, blank=True, null=True)
    booked_on = models.DateField(auto_now=True)