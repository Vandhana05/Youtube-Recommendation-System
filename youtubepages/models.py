# from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class SearchForm(models.Model):
    search=models.CharField(max_length=300)
    class Meta:
        # create a name for Table
        db_table='UserSearch'



# Create your models here.
class VideoForm(models.Model):
    CategoryId=models.CharField(max_length=30)
    Category=models.CharField(max_length=30)
    ChannelName=models.CharField(max_length=80)
    Title=models.CharField(max_length=200)
    video = models.FileField(null=True, verbose_name="")

    class Meta:
        # create a name for Table
        db_table='YoutubeVideo'
    

# Create your models here.
class createuserForm(models.Model):
    Name=models.CharField(max_length=50)
    EmailId=models.EmailField()
    Password=models.CharField(max_length=20)
    Gender=models.CharField(max_length=10)
    ChannelName=models.TextField(max_length=60)
    ProfileImage=models.ImageField(null=True,blank=True)
    Search=models.TextField(null=True)
    

    class Meta:
        db_table='UserDetails'

    