from django.db import models


class Employee(models.Model):
    eid = models.IntegerField()
    name = models .CharField(max_length= 40)
    image = models.ImageField(upload_to="Assets/my_images")

    def __str__(self):
        return self.name
