"""
Definition of models.
"""

from django.db import models

class Queries(models.Model):
    username = models.CharField(max_length=255)
    query = models.CharField(max_length=255)

