from django.db import models

# Create your models here.
class Skill(models.Model):
    name= models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Offer_list(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
   
    def __str__(self):
        return self.title   
    


class Employe(models.Model):
    designation = models.CharField(max_length=100)
    education = models.TextField(help_text="List degrees, certifications, or qualifications")
    expertise = models.TextField(help_text="Describe skills, technologies, and areas of expertise")

    def __str__(self):
        return self.designation


class Career(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
  