from django.db import models
from django.utils.html import format_html
# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    image1 = models.ImageField(upload_to="image/")
    pdis1 = models.TextField()
    image2 = models.ImageField(upload_to="image/")
    ptitle = models.CharField(max_length=100)
    pcat = models.ForeignKey(Cat,on_delete= models.CASCADE)
    pdis2 = models.TextField()
    
    def image_tag(self):
        return format_html('<img src="\media\{}"  />'.format(self.image1))

class register(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
class total_views(models.Model):
    uid = models.IntegerField(max_length=10)
    pid = models.IntegerField(max_length=10)
    

     