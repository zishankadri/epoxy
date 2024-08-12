from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

import os


class GalleryItem(models.Model):
    FILE_TYPE_CHOICES = [
        ("IMAGE", "Image"),
        ("VIDEO", "Video"),
    ]
    # content = CloudinaryField('content')
    content = models.FileField(upload_to="gallery/", max_length=100)
    file_type = models.CharField(choices=FILE_TYPE_CHOICES, max_length=10)
    rank = models.IntegerField()

    def get_extension(self):
        name, extension = os.path.splitext(self.content.name)
        return extension.lower()


class Contact(models.Model):

    CONTACT_METHOD_CHOICES = (
        ("CALL", "Call"),
        ("WHATSAPP", "WhatsApp"),
        ("EMAIL", "Email"),
    )
    
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    message = models.TextField()
    image = models.FileField(upload_to="contact_media/", max_length=100, blank=True, null=True) # Optional image field

    contact_method = models.CharField(choices=CONTACT_METHOD_CHOICES, max_length=50)
    
    def __str__(self):
        return f"{self.full_name}"
