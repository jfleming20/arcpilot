from django.db import models


class DjangoClaim(models.Model):
    uuid = models.CharField(max_length=36, unique=True, primary_key=True)
    claim_id = models.CharField(max_length=255)
    claim_status = models.CharField(max_length=255)
    claimant_name = models.CharField(max_length=255)
    claim_amount = models.CharField(max_length=255)
    claim_date = models.CharField(max_length=255)
    claim_closure_date = models.CharField(max_length=255)
    claim_documents = models.CharField(max_length=255)
