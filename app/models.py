from django.db import models
# Register your models here.
class send(models.Model):
    Email=models.CharField(max_length=150,help_text='User name')
    Date=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Email

class contect(models.Model):
    Username=models.CharField(max_length=70, help_text="username")
    Email=models.CharField(max_length=150,help_text="Email")
    Message=models.TextField(max_length=500)
    Date=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Username

class resume(models.Model):
    url= models.CharField(max_length =350,default="")
    

class certificate(models.Model):
    Topic=models.CharField(max_length=70)
    Image=models.ImageField(upload_to="app/image",default='')            

    def __str__(self):
        return self.Topic

class project(models.Model):
    Project_name=models.CharField(max_length=70)
    Github_url=models.CharField(max_length=300,default='')
    Image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.Project_name        