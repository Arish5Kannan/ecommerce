from django.db import models
import os
import datetime
def getFilename(request,filename):
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    new_filename = '%s%s'%(now,filename)
    return os.path.join('uploads/',new_filename)
class Category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)  
    image = models.ImageField(upload_to=getFilename,null=True,blank=True) 
    description = models.TextField(max_length=500,null=False,blank=False) 
    status = models.BooleanField(default=False,help_text='0-show,1-hidden')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)  
    vendor = models.CharField(max_length=150,null=False,blank=False) 
    quantity = models.IntegerField(null=False,blank=False) 
    old_price = models.FloatField(null=False,blank=False)
    new_price =  models.FloatField(null=False,blank=False)
    product_image = models.ImageField(upload_to=getFilename,null=True,blank=True) 
    description = models.TextField(max_length=500,null=False,blank=False) 
    status = models.BooleanField(default=False,help_text='0-show,1-hidden')
    trending = models.BooleanField(default=False,help_text='0-default,1-trending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name        