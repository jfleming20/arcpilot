from django.db import models


class DjangoPaymentMethod(models.Model):
    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
    payment_type = models.CharField(max_length=255)
    payment_details = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    payment_validation = models.CharField(max_length=255)
