from django.db import models
from django.conf import settings

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
