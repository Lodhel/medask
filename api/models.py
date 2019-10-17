from django.db import models


class Main(models.Model):
    TYPE_CHOICES = [('dms', 'dms'), ('oms', 'oms')]
    type = models.CharField(
        max_length=3, choices=TYPE_CHOICES, default="dms"
    )
    number = models.CharField(max_length=32)
    company = models.CharField(max_length=128)
    service = models.CharField(max_length=256)

    class Meta:
        db_table = 'main'

    def __str__(self):
        return str(self.pk)