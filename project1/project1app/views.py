from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Group
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    team = Group.objects.all()
    return render(request,"index.html",{'result':obj,'teams':team})
def login(request):
    return render(request,"login.html")
