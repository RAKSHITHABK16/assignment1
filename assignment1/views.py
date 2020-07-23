from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Welcome To The Project</marquee>")

def grt(request,grt):
    b=grt.split(" ")
    if int(b[0]) > int(b[1]):
        return HttpResponse(str(b[0]))
    else:
        return HttpResponse(str(b[1]))

def grt3(request,x,y,z):
    if int(x > y) and int(x > z):
        return HttpResponse("The greatest value is {}".format(x))
    elif int(y > x) and int(y > z):
        return HttpResponse("The greatest value is {}".format(y))
    else:
        return HttpResponse("The greatest value is {}".format(z))

def vc(request,str):
    v="aeiouAEIOU"
    vowels=0
    consonants=0
    for i in str:
        if i in v:
            vowels += 1
        else:
            consonants += 1
            
    return render(request,"directory/v&c.html",{"string":str,"vowels":vowels,"consonants":consonants})    
