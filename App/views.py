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
    return render(request,'login.html',{})
