from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class State(models.Model):
      state = models.CharField(max_length=255)
      def __str__(self):
           return self.state
      
class Season(models.Model):
     season=models.CharField(max_length=255)
     def __str__(self):
          return self.season

class Destinations(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Image = CloudinaryField('image')
    season = models.ForeignKey(Season,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    def __str__(self):
           return self.state
    
class Restaurants(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    food = models.TextField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.state
    
class login_form(models.Model):
     username = models.CharField(max_length=255)
     email = models.EmailField()
     password = models.CharField(max_length=255)
     c_password = models.CharField(max_length=255)

     def __str__(self):
          return self.username
    
class contact_us(models.Model):
      First_name = models.CharField(max_length=255)
      Last_name = models.CharField(max_length=255)
      Contact_no = models.IntegerField()
      Email_id = models.EmailField()
      Message = models.TextField()

      def __str__(self):
          return self.First_name

class profileimage(models.Model):
     image = CloudinaryField('image')
     nimg  = models.CharField(max_length=266)


      