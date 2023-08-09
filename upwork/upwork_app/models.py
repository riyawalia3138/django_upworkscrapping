from django.db import models

class upwork(models.Model):
    up_name = models.CharField(max_length=50, null=True, blank=False)
    limit = models.IntegerField(null=True, blank=False)

class my_table(models.Model):
    upwork_entry = models.ForeignKey('upwork', on_delete=models.CASCADE )
    JobName = models.TextField(null=True, blank=False)
    JobDescription = models.TextField(null=True, blank=False)  

class dataa(models.Model):
    my_table_entry = models.ForeignKey('my_table', on_delete=models.CASCADE)
    data_skills = models.TextField(null=True, blank=False)  



# from django.db import models

# # Create your models here.
# class upwork(models.Model):
#     up_name= models.CharField(max_length=50, null=True, blank=False)
#     limit=models.IntegerField(null=True, blank=False)  
    
#     def __str__(self,key):
#         return self.__dict__[key]
    
# class my_table (models.Model):
#     JobName=models.TextField(null=True, blank=False)
#     JobDescription=models.TextField(null=True, blank=False)

# class dataa(models.Model):  
#     data_skills=models.TextField(null=True, blank=False)        