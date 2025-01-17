from django.db import models


class DjangoLead(models.Model):
    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
