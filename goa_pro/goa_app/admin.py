from django.contrib import admin
from .models import Destinations,Season,State,Restaurants,login_form,contact_us,profileimage

# Register your models here.

admin.site.register(Destinations)
admin.site.register(State)
admin.site.register(Season)
admin.site.register(Restaurants)
admin.site.register(login_form)
admin.site.register(contact_us)
admin.site.register(profileimage)





