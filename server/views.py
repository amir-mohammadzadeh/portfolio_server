from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def seyHello(request):
    data = [
        {"id":1,"name":"mamad"},
        {"id":2,"name":"ali"},
    ]
    return JsonResponse(data,safe=False)

