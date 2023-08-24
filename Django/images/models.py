from django.db import models
import os

class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return os.path.basename(self.image.name)