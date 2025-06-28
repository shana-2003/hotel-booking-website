from django.contrib import admin
from .models import menu,deals,booking
# Register your models here
admin.site.register(menu)
admin.site.register(deals)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','c_name','c_phone','c_email','booking_date','booking_time','no_guest','seating_pref','sp_request','booked_on')
admin.site.register(booking, BookingAdmin)
