from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone_number', 'product_detail']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')
