from django.db import models



# Create your models here.
class facultyMember(models.Model):
    name = models.CharField(max_length=10)
    mail = models.EmailField(max_length=20)
    branch = models.CharField(max_length=5)
    age =  models.IntegerField()
    gender_list = [('Male', 'Male'),('Female','Female')]
    gender = models.CharField(choices=gender_list,max_length=7 ,null=True,blank=True)
    password = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name
