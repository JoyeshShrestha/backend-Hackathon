from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from user_profile.models import UserProfile
class ItemListing(models.Model):
    CONDITION_CHOICES = (
        ('Brand New', 'Brand New'),
        ('Like New', 'Like New'),
        ('Used', 'Used'),
    )

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    availability_status = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Price field as a decimal
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)  # Image field
   
    def __str__(self):
        return self.title
