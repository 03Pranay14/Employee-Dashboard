from django.db import models
# Create your models here.
class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200,blank=False,null=False)
    email=models.EmailField(max_length=200,blank=False,null=False,default=None)
    role = models.CharField(max_length=100,default=None)
    gender = models.CharField(max_length=100,blank=False,null=False,default=None)

    def __str__(self):
        return (f"{self.id} {self.name} ")
    

class staff(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Email=models.EmailField()
    Role=models.CharField(max_length=255)
    Address=models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name

class contact_details(models.Model):
    name_contact=models.CharField(max_length=50)
    phone_of_contact=models.IntegerField()
    email_of_contact=models.EmailField()
    address_of_contact=models.TextField(max_length=500)
    subject_of_contact=models.CharField(max_length=100)
    message_of_contact=models.TextField(max_length=1000)
    
    def __str__(self):
        return (f"{self.id} {self.name_contact}")
    
    
    
    
 

