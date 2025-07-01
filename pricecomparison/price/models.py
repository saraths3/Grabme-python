from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='product_images/')

    def __str__(self):
        return self.name

# Create your models here.
