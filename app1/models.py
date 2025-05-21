from django.db import models

class Employee(models.Model):  # table
    name = models.CharField(max_length=50)   #attribute -> fields
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    designation = models.CharField(max_length=50,default="") 

    def __str__(self):
        return self.name

# makemigrations  ->
# python class -------------------------------->python class(migration sub-package)
                                              # schema define (logically)

# migrate ->                                            table
# python class(migration sub-package)-------------------->physical table 

# createsuperuser 