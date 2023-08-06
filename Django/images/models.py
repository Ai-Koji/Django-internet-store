from django.db import models
import os

class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return os.path.basename(self.image.name)

class Main_slider(models.Model):
    image = models.ImageField(upload_to="images/")
    urlTo = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.name
    def get_cells(self): # getting cells for page rendering
        return {"name": self.name,
            "image": "/media/images/" + os.path.basename(str(self.image)),
            "urlTo": self.urlTo
            }
    