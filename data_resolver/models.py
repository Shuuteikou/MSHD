from django.db import models

# Create your models here.
class CommDisaster(models.Model):
    id = models.CharField(max_length=19,primary_key=True)

    date = models.CharField(max_length=12)

    location = models.CharField(max_length=100)

    type = models.CharField(max_length=4)

    grade = models.CharField(max_length=4)

    picture = models.BinaryField(max_length=1024 * 1024 * 8)

    note = models.CharField(max_length=200)

    reporting_unit=models.CharField(max_length=50)