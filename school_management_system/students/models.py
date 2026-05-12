from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.IntegerField(primary_key= True, unique= True)
    name = models.CharField(max_length= 50, verbose_name= 'Student Name')
    age = models.IntegerField(null=True, blank=True)
    fName = models.CharField(max_length= 50)

    def __str__(self):
        return f"{self.name}, {self.id}"