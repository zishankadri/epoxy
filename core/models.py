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

