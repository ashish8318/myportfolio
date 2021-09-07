from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.core.mail import send_mail 
from validate_email import validate_email
from .models import send,resume,contect,certificate,project
import datetime
# import requests
import json
import os
import requests
def index(request):
    c=certificate.objects.all()
    p=project.objects.all()
    return render(request,"index.html",{"project":p,"certificate":c})
def sendlink(request):
    tday=datetime.date.today()
    email=request.POST["email"]
    is_valid = validate_email(email)
    if(is_valid):
        q=resume.objects.all()
        url=' '
        for i in q:
            url=i.url
        mail=send_mail("Download Resume"," ",os.environ.get('send_email'),[email],html_message='''<p>Thanks for visit my portfolio <br>Please click link to download Resume </p><a href="{}" target='_blank' download>Download</a>'''.format(url))
        if mail:
            s=send(Email=email,Date=tday)
            s.save()
            messages.info(request,"Link send to your email pelase download")
            return redirect("index") 
    else:
        messages.error(request,"Please enter valid Email")
        print("asdsafdsf")
        return redirect("index") 

    return render(request,"index.html")

def contectmessage(request):
    email2=''
    tday=datetime.date.today()
    if(len(request.POST["username"])==0):
        messages.error(request,"Username required")
    else:
        username=request.POST["username"]
    if(len(request.POST["email"])==0):
        messages.error(request,"Email required")
    else:
        email=request.POST["email"]
        if(validate_email(email)):
            email2=email
        else:
            messages.error(request,"Invalid Email")

    if(len(request.POST["message"])==0):
        messages.error(request,"message required")
    else:
        message=request.POST["message"]        
    
    recaptcha_response=request.POST.get("g-recaptcha-response")
    data = {
                'secret': os.environ.get('recaptcha_secret') ,
                'response': recaptcha_response
            }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()    
    if result['success']:
        if(len(username)!=0 and len(email2)!=0 and len(message)!=0):
            obj=contect(Username=username,Email=email,Message=message,Date=tday)
            obj.save()
            messages.info(request,"Thanks for contect") 
            send_mail("Portfolio Contect"," ",os.environ.get('send_email'),[os.environ.get('receive_email')],html_message='''<p>Username: {}</p> <p>Email: {}</p><p>Message: {}</p>'''.format(username,email,message))       
            return redirect("index")
    else:
        messages.error(request,"Recaptcha error")
        return redirect("index")
