from django.db import models

class UserProfile(models.Model):
   
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=255,default='')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=15)  # Assuming a typical phone number length
   
   
    def __str__(self):
        return self.user_name
