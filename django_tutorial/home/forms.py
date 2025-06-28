
from django import forms
  
from .models import booking


class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        widgets = {
            'booking_date':DateInput(),
            'booking_time':TimeInput(),
        }
        labels={
            'c_name': "Your Name:",
            'c_phone': "Contact Number:",
            'c_email': "Email Address(for confirmation):",
            'booking_date': "Reservation Date:",
            'booking_time': "Preferred Dining Time:",
            'no_guest': "How Many People?:",
            'seating_pref': "Choose Your Spot:",
            'sp_request': "	Any Special Requests?:",
        }