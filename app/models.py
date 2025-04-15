from django.db import models
from .utility import find_max_rank
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
  
        
          
class Skill(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    tecnology = models.ForeignKey(Skill,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(default=find_max_rank)
    is_active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
class Hero(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title

class Social(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    
    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    
    def __str__(self):
        return self.name
    