from django import forms
from .models import Destinations,Restaurants,contact_us,profileimage

class Destinations_form(forms.ModelForm):
    class Meta:
        model = Destinations
        fields = '__all__'


class Restaurants_form(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = '__all__'
        
class contact_us_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

class profileimageform(forms.ModelForm):
    class Meta:
        model = profileimage
        fields = '__all__'

