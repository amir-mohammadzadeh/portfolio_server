from django.shortcuts import render
from django.http import JsonResponse,QueryDict,HttpResponse
from .models import * 
import json
from django.core.serializers import serialize 
# Create your views here.

def index(request):
    return render(request,"index.html")

def readeJsonFile():
    with open('media/data.json','r',encoding="utf-8") as file:
        r = file.read()
        JSON_DATA= json.loads(r)
    return JSON_DATA

def seyHello(request):

    data = [
        {"id":1,"name":"mamad"},
        {"id":2,"name":"ali"},
    ]
    return JsonResponse(data,safe=False)

def getSiteInfo(request):
    #data =SiteInfo.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['siteInfo']
    
    return JsonResponse(result,safe=False)


def getSiteMenu(request):
    data =SiteMenu.objects.all()

    result = list(data.values())

    return JsonResponse(result,safe=False)


def getMyInformation(request):
    #data =AboutMe.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['AboutMe']


   
    return JsonResponse(result,safe=False)


def getSiteDocuments(request):
    #data =SiteDocuments.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['SiteDocuments']

    return JsonResponse(result,safe=False)


def getMyServices(request):
    #data =Services.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['Services']
    

    return JsonResponse(result,safe=False)


def getClientslist(request):
    #data =Clients.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['Clients']
    

    return JsonResponse(result,safe=False)


def getJobExperience(request):
    #data =JobExperience.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['JobExperience']
    

    return JsonResponse(result,safe=False)


def getEducationQuality(request):
    #data =EducationQuality.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['EducationQuality']
    

    return JsonResponse(result,safe=False)


def getMySkills(request):
    #data =Skill.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['Skills']
    

    return JsonResponse(result,safe=False)


def getMyPortflios(request):
    #data =Portflios.objects.filter(status=True)

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['portfolios']
    

    return JsonResponse(result,safe=False)


def getPortfolioImages(request):
    #data =PortfolioImages.objects.filter(portfolioId= 1)

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['portfoliosImages']

    return JsonResponse(result,safe=False)


def getPortfolioDetailesById(request, id):
    #data =PortfolioDetailes.objects.filter(portfolioId= 1)

    #result = list(data.values())
    jd=readeJsonFile()
    r = jd['PortfolioDetailes']
    result={}
    for item in r:
        if item['id'] == id :
            result = item
            break


    return JsonResponse(result,safe=False)


def getMyConntactInfo(request):
    #data =ConntactInfo.objects.all()

    #result = list(data.values())

    jd=readeJsonFile()
    result = jd['contactInfo']
    

    return JsonResponse(result,safe=False)
