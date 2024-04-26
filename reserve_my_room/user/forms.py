from django import forms
from django import forms
from hotel.models import hotel_hoteldetails

from user.models import room_details


class ContactForm(forms.Form):
    email = forms.EmailField()


class hoteldetailsform(forms.ModelForm):
    class Meta:
        model = hotel_hoteldetails
        fields = '__all__'

class roomdetailsform(forms.ModelForm):
    class Meta:
        model = room_details
        fields = '__all__'