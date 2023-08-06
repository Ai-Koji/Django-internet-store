from django.db import models

class BaseRequest(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=30)
    message = models.TextField()
    sended_to_mail = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.username}, {self.email}"

class Offer(BaseRequest):
    product = models.CharField(max_length=30)

class ServiceOffer(BaseRequest):
    service_name = models.CharField(max_length=30)

class Contact(BaseRequest):
    pass

class Question(BaseRequest):
    pass