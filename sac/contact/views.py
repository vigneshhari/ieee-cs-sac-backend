from django.shortcuts import render
from django.http import JsonResponse
from .models import contact
import datetime


def contactnew(request):
    if(request.method == "GET"):
        name = request.GET.get("name",'')
        phno = request.GET.get("phno",'')
        email = request.GET.get("email",'')
        message = request.GET.get("message",'')
        if(name == "" or phno == "" or email == "" or message == ""):
            return JsonResponse({"Response Code" : "02" , "Message" : "Invalid Data Provided"})
        try:
            test = contact(name = name , phno = phno , email = email , message = message , time = datetime.datetime.now() )
            #Email Logic
            test.save()
        except Exception as e:
            print e 
            return JsonResponse({"Response Code" : "04" , "Message" : "Error in Email/Database Server"})
        return JsonResponse({"Response Code" : "01" , "Message" : "Sucessfully Saved Data"})
    else:
        return JsonResponse({"Response Code" : "03" , "Message" : "This Server works on GET Requests"})