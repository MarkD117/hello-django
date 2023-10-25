from django.db import models

# Create your models here.


class Item(models.Model):
    # null=False prevents the field from being blank programmatically
    # blank=False prevents the field from accepting if left blank
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Changing the default string name of our created items to the name set
    def __str__(self):
        return self.name
