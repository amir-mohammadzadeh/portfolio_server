from django.db import models

# Create your models here.


class SiteInfo(models.Model):
    LANGS = (
        ('fa','فارسی'),
        ('en','English')
    )
    THEME = (
        ('dark','Dark'),
        ('light','Light')
    )
    title= models.CharField(max_length=250)
    helloText=models.TextField()
    language = models.CharField(max_length= 25 , choices=LANGS , default='fa')
    theme = models.CharField(max_length= 25 , choices=THEME , default='dark')
    logo= models.ImageField(upload_to='test/',name='logooo')
    headerImage= models.ImageField(upload_to='test/',name='header')

    def __str__(self):
        return self.title
        