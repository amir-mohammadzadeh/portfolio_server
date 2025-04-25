from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,EMPTY_VALUES

# Create your models here.



#  Site Information
class SiteInfo(models.Model):
    LANGS = (
        ('fa','فارسی'),
        ('en','English')
    )
    THEME = (
        ('dark','Dark'),
        ('light','Light')
    )
    language = models.CharField(max_length= 25 , choices=LANGS , default='fa')
    title= models.CharField(max_length=250)
    headerText=models.TextField(blank=True)
    theme = models.CharField(max_length= 25 , choices=THEME , default='dark')

    def __str__(self):
        return self.title
        
#  Site Menu
class SiteMenu(models.Model):
    title= models.CharField(max_length=50)
    title_en= models.CharField(max_length=50)
    icon = models.ImageField(upload_to="icons/")
    url=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
        

# Information of me
class AboutMe(models.Model):
    LANGS = (
        ('fa','فارسی'),
        ('en','English')
    )
    lang=models.CharField(max_length= 25 , choices=LANGS , default='fa')
    name=models.CharField(max_length=25)
    family=models.CharField(max_length=25)
    expertise=models.CharField(max_length=250)
    email= models.EmailField(max_length=100)
    phoneNumber=models.BinaryField(max_length=11,help_text='09*********')
    birthday=models.IntegerField()
    address = models.CharField(max_length=250)
    aboutMe=models.TextField(max_length=1500)
    points = models.CharField(max_length=250 , help_text='Examp: item1 - item2 - ...' , blank=True)
    gitHubLink = models.CharField(max_length=100)
    linkedinLink = models.CharField(max_length=100)
    telegramLink = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " +  self.family

# Image and files of site
class SiteDocuments(models.Model):
    logo=models.ImageField(upload_to="webSite/")
    headerImage=models.ImageField(upload_to="webSite/")
    profile=models.ImageField(upload_to="webSite/")
    profileImage=models.ImageField(upload_to="webSite/")
    rezumePDF=models.FileField(upload_to="" , blank=True)

    
#  My Sosial linkes
#class SosialMedia(models.Model):
#    ICONS = (
#        ('Linkedin','Linkedin'),
#        ('Telegram','Telegram'),
#        ('Github','Github'),
#        ('Instagram','Instagram'),
#    )
#        
#    title= models.CharField(max_length=50)
#    icon = models.CharField(max_length=50, choices=ICONS)
#    url=models.CharField(max_length=50)
#    
#    def __str__(self):
#        return self.title
     

# My Service
class Services(models.Model):
    title=models.CharField(max_length=50)
    title_En=models.CharField(max_length=50)
    discription=models.TextField(max_length=250)
    discription_En=models.TextField(max_length=250)
    icon=models.ImageField(upload_to="icons/")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title



# Client List
class Clients(models.Model):
    clientName=models.CharField(max_length=50)
    clientName_En=models.CharField(max_length=50)
    image=models.ImageField(upload_to="customers/")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.clientName



#  Job Experience
class JobExperience(models.Model):
    LANGS = (
        ('fa','فارسی'),
        ('en','English')
    )

    lang=models.CharField(max_length= 25 , choices=LANGS , default='fa')   
    title= models.CharField(max_length=50)
    start_From= models.IntegerField()
    end_At= models.IntegerField()
    companyName = models.CharField(max_length=50)
    discription = models.TextField(max_length=250 , blank=True)


    def __str__(self):
        return self.lang



#  Education Quality
class EducationQuality(models.Model):
    LANGS = (
        ('fa','فارسی'),
        ('en','English')
    )

    lang=models.CharField(max_length= 25 , choices=LANGS , default='fa')
    title= models.CharField(max_length=50)
    start_From= models.IntegerField()
    end_At= models.IntegerField()
    companyName = models.CharField(max_length=50 , help_text="School or University name...")
    discription = models.TextField(max_length=250, blank=True)
    
    
    def __str__(self):
        return self.lang


#  Skill
class Skill(models.Model):
    title = models.CharField(max_length=25)
    value = models.IntegerField(help_text="Between 1 and 5",validators=[MinValueValidator(0) ,MaxValueValidator(5)])

    def __str__(self):
        return self.title
    


# Portfolios
class Portflios(models.Model):
    title = models.CharField(max_length=50)
    title_En = models.CharField(max_length=50)
    shortDiscriptin= models.TextField(max_length=150)
    shortDiscriptin_En= models.TextField(max_length=150)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Portfilio Images
class PortfolioImages(models.Model):
    portfolioId = models.ForeignKey(Portflios ,on_delete=models.CASCADE, related_name="Portfolio_images")
    desktopImage=models.ImageField(upload_to="Portfolio/")
    mobileImage = models.ImageField(upload_to="Portfolio/")

    
    def __str__(self):
        return self.portfolioId


# Portfolio Detiales
class PortfolioDetailes(models.Model):
    portfolioId = models.ForeignKey(Portflios ,on_delete=models.CASCADE, related_name="Portfolio_detailes")
    longDiscriptin= models.TextField(max_length=500)
    longDiscriptin_En= models.TextField(max_length=500)
    skillsUsed=models.TextField(help_text="Examp: item1, item2, ...")
    likeCount = models.IntegerField(default=0 , blank= True)
    disLikeCount = models.IntegerField(default=0 , blank= True)
    PreviewLink = models.CharField(max_length=150, blank= True)
    sourceLink = models.CharField(max_length=150, blank= True)
    

    def __str__(self):
        return self.portfolioId


# Contact with me
class ConntactInfo(models.Model):
    email= models.EmailField(max_length=100)
    phoneNumber=models.BinaryField(max_length=11,help_text='09*********')
    discription=models.TextField(max_length=250)
    discription_En=models.TextField(max_length=250)
    job=models.CharField(max_length=50)
    job_En=models.CharField(max_length=50)

    def __str__(self):
        return self.phoneNumber


