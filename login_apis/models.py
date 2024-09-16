from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=1234)
    email = models.EmailField(default="default_email@example.com")
    
    password=models.TextField(max_length=13456)
# class candiates(models.Model):
#        name=models.CharField(max_length=12345678)
#        postion=models.CharField(max_length=1234356478)


# class create_elections(models.Model):
#     organizer=models.ForeignKey(users,on_delete=models.CASCADE)
#     title=models.CharField(max_length=12345678,default="")
#     number_of_candidates=models.IntegerField(default=0)