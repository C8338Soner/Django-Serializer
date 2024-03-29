from django.db import models


class Path(models.Model):
 path_name= models.CharField(max_length=30)
 
 def __str__(self):
  return self.path_name

class Student(models.Model):
 path = models.ForeignKey(Path, related_name = 'students', on_delete=models.CASCADE)
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100)
 number = models.IntegerField(blank=True, null=True)
 
 def __str__(self):
  return f"{self.first_name} {self.last_name}"