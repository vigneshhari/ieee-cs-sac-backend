from django.shortcuts import render
from django.http import JsonResponse
from .models import contact
import datetime


def contactnew(request):
    if(request.method == "POST"):
        print "YAY"
        name = request.POST.get("name",'')
        phno = request.POST.get("phno",'')
        email = request.POST.get("email",'')
        message = request.POST.get("message",'')
        try:
            test = contact(name = name , phno = phno , email = email , message = message , time = datetime.datetime.now() )
            #Email Logic
            test.save()
        except:
            return JsonResponse({"Response Code" : "04" , "Message" : "Error in Email/Database Server"})
    else:
        return JsonResponse({"Response Code" : "03" , "Message" : "This Server works on POST Requests"})