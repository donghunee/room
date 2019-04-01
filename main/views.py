from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import auth
from .models import Upload
# Create your views here.


def main(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'],password=request.POST['password1']
            )
            auth.login(request, user)
            return redirect('main')
    return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('main')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    return render(request,'login.html')



def upload(request):
    if request.method == 'POST':
        upload = Upload()
        upload.username = request.user.username
        upload.name = request.POST['name']
        upload.sex = request.POST['sex']
        upload.time = request.POST['time']
        upload.attention = request.POST['attention']
        upload.person = request.POST['person']
        upload.one = request.POST['one']
        upload.two = request.POST['two']
        upload.thr = request.POST['thr']
        
        upload.save()   
        return redirect("show")
    return render(request,'upload.html')



def match(request):
    
    my = Upload.objects.get(username = request.user.username)
    match = ""
    
    max = 0
    one = my.one
    two = my.two
    thr = my.thr
    
    for x in Upload.objects.exclude(username = my.username):
        result = 0
        if one == "time":
            if my.time == x.time:
                result += 10
        elif one == "person":
            if my.person == x.person:
                result += 10 
        else:
            if my.attention == x.attention:
                result += 10

        if two == "time":
            if my.time == x.time:
                result += 5
        elif two == "person":
            if my.person == x.person:
                result += 5 
        else:
            if my.attention == x.attention:
                result += 5

        if thr == "time":
            if my.time == x.time:
                result += 3
        elif thr == "person":
            if my.person == x.person:
                result += 3 
        else:
            if my.attention == x.attention:
                result += 3

        if result >= max:
            match = x.name
            max = result
    max = round((max/18)*100,2)
    return render(request,'show.html',{'match' : match,'max':max })

    


        
       
        


