from django.db import models


class Model(models.Model):
    title = models.CharField(max_length=50, null=False)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField(null=False)
