from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.TextField()
    email = models.EmailField(null=True)
    telegram = models.TextField()
    telegram_id = models.PositiveIntegerField(unique=True)
    phone_number = models.TextField()
    paid_to = models.DateField()


class Customer(models.Model):
    external_id = models.PositiveIntegerField(unique=True)
    telegram = models.TextField(null=True)


class CustomerMessage(models.Model):
    message_id = models.PositiveIntegerField()
    chat_id = models.PositiveIntegerField()


class CompanyReply(models.Model):
    message_id = models.PositiveIntegerField()
    chat_id = models.PositiveIntegerField()
    reply_to = models.ForeignKey(CustomerMessage, on_delete=models.CASCADE)
