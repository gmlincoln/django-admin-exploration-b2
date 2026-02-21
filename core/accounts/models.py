from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    dept = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    student_id = models.IntegerField()
    address = models.TextField(max_length=200)
    image = models.ImageField(upload_to='student_img/', null= True, blank=True)