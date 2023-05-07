from django.db import models


class Men(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    content = models.TextField(blank=True)