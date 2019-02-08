from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from App.models import person

from django.http import HttpResponse

@csrf_exempt
def register(request):
    if(request.method=="POST"):
        context={}
        context['username']=request.POST['username']
        context['password']=request.POST['password']
        context['email']=request.POST['email']
        context['user_type']=request.POST['user_type']

        if person.objects.filter(username=context['username']).exists():
            context['message']="Username already exists"
            return render(request,'reg.html',context)
        else:
            obj=person(username=context['username'], password=context['password'], email=context['email'], user_type=context['user_type'])
            obj.save()
            return redirect('/login')
    else:
        return render(request,'reg.html',{})


# Create your views here.
@csrf_exempt
def login(request):
    if('username' in request.session):
        uname = request.session['username']
        utype = request.session['user_type']

        if(utype=='Student' or utype=='student'):
            return redirect('/studentDashboard')
        else:
            return redirect('/recruiterDashboard')

    if(request.method=="POST"):
        context={}
        context['username']=request.POST['username']
        context['password']=request.POST['password']

        if(person.objects.filter(username=context['username']).exists()):
            if(person.objects.filter(username=context['username'] , password=context['password'])):
                person_objects = person.objects.get(username=context['username'])

                if(person_objects.user_type=="Student" or person_objects.user_type=="student"):
                    request.session['username']=person_objects.username
                    request.session['user_type']=person_objects.user_type
                    return redirect('/studentDashboard')
                elif(person_objects.user_type=="Recruiter" or person_objects.user_type=="recruiter"):
                    request.session['username']=person_objects.username
                    request.session['user_type']=person_objects.user_type
                    return redirect('/recruiterDashboard')
            else:
                context={}
                context['message']="Invalid password"
                return render(request,'login.html',context)

        else:
            context={}
            context['message']="Username does not exists"
            return render(request,'login.html',context)
    else:
        return render(request,'login.html',{})

@csrf_exempt
def stuDashboard(request):
    return render(request,'studentDashboard.html',{})

@csrf_exempt
def logout(request):
    if('username' in request.session):
        del request.session['username']
        del request.session['user_type']
    return redirect('/login')

@csrf_exempt
def recDasboard(request):
    return render(request,'recruiterDashboard.html',{})


    #return render(request,'login.html',{})
