from django.db import models

# Create your models here.
class register(models.Model):
    studentName = models.CharField(max_length=10)
    mail = models.EmailField()
    password = models.CharField(max_length=8)
    gender_list = [('Male', 'Male'),('Female','Female')]
    gender = models.CharField(choices=gender_list,max_length=7 ,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)   
    branch = models.CharField(max_length=7,null=True,blank=True) 
    def __str__(self) -> str:
        return self.studentName
    
class library(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=30)
    book_author = models.CharField(max_length=15)
    publication_date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='library/')
    
    def __str__(self) -> str:
        return self.book_name
    