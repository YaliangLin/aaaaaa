from django.http import HttpResponse
import random
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from django.db.models import Sum, Count
from .models import biaoge
import datetime
import json
from django.forms import ModelForm
from .forms import SquirrelForm
from .forms import SquirrelImages
from .models import images
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO
from django.views.generic import View
from django.shortcuts import get_object_or_404 



def main(request):
    squirrels = biaoge.objects.order_by('Unique_Squirrel_ID')
    number = biaoge.objects.count()
    context = {'squirrels':squirrels,
               'number': number,
    }

    return render(request,'htmls/test.html',context)

def map(request):
    sighting100 = random.sample(list(biaoge.objects.all()),100)
    sighting_list = []
    for sighting in sighting100:
        sighting_list.append({'xx':sighting.xx,'yy':sighting.yy})
    context = {'sightings':sighting_list,}
    return render(request,'htmls/map.html',context)

def edit(request, squirrel_id):
    squirrel = biaoge.objects.get(pk = squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/success')
    else:
        form = SquirrelForm(instance = squirrel)
        context = {'form':form,}
    return render(request,'htmls/edit.html',context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/success')
    else:
        form = SquirrelForm()
        context = {'form':form,}
    return render(request,'htmls/add.html',context)


def status(request, squirrel_id):
    squirrels = biaoge.objects.get(pk = squirrel_id)
    context = {'squirrel_id':squirrel_id,
                'alldata':squirrels
    }
    return render(request,'htmls/status.html',context)
    
def success(request):
    return render(request,'htmls/success.html')

def test(request):
    return render(request,'htmls/test.html')

def good(request):
    squirrels = biaoge.objects.filter(have_image = True)
    activities = ['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Kuks', 'Quaas', 'Moans', 'Other activities','Approaches','Tail Twitches','Runs from','Nothing']
    context ={'squirrels':squirrels,
              'activities': activities
    }
    return render(request,'htmls/mainbase.html',context)

def goodadd(request):
    # 判断是否为 post 方法提交 
    if request.method == "POST":
    #load things from web
        latitude = request.POST.get('latitude',0)
        longtitude = request.POST.get('longtitude',0)
        Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID',00-0000-00-00)
        shift = request.POST.get('shift',None)
        date = request.POST.get('date',None)
        age = request.POST.get('age',None)
        primary_fur_color = request.POST.get('primary_fur_color',None)
        location = request.POST.get('location',None)
        specific_location = request.POST.get('specific_location',None)
        running = request.POST.get('running',False)
        chasing = request.POST.get('chasing',False)
        climbing = request.POST.get('climbing',False)
        eating = request.POST.get('eating',False)
        foraging = request.POST.get('foraging',False)
        other_activities = request.POST.get('other_activities',None)
        kuks = request.POST.get('kuks',False)
        quaas = request.POST.get('quaas',False)
        tail_flags = request.POST.get('tail_flags',False)
        tail_twitches = request.POST.get('tail_twitches',False)
        approaches = request.POST.get('approaches',False)
        indifferent = request.POST.get('indifferent',False)
        runs_from = request.POST.get('runs_from',False)
        #request.FILES.get('profile_image',None)
        moans = request.POST.get('moans',False)
        have_image = request.POST.get('have_image',False)
        test1 = biaoge.objects.create(xx = latitude,
            yy = longtitude,
            Unique_Squirrel_ID = Unique_Squirrel_ID,
            shift = shift,
            date =date,
            age =age,
            primary_fur_color =primary_fur_color,
            location =location,
            specific_location =specific_location,
            running =running,
            chasing =chasing,
            climbing =climbing,
            eating =eating,
            foraging =foraging,
            other_activities =other_activities,
            kuks =kuks,
            quaas =quaas,
            tail_flags =tail_flags,
            tail_twitches =tail_twitches,
            approaches =approaches,
            indifferent =indifferent,
            runs_from =runs_from,
            moans =moans,
            profile_image = request.FILES.get('profile_image',None),
            have_image =have_image,
        )
        test1.save()
        return redirect(f'/success')
    else:
        context= {'sssss':'sssss.jpg'}
        return render(request, 'htmls/checkout.html',context)


def goodedit(request,squirrel_id):
    test1 = biaoge.objects.get(pk = squirrel_id)
    if request.method == "POST":
        latitude = request.POST.get('latitude',0)
        longtitude = request.POST.get('longtitude',0)
        Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID',00-0000-00-00)
        shift = request.POST.get('shift',None)
        date = request.POST.get('date',1111-11-11)
        age = request.POST.get('age',None)
        primary_fur_color = request.POST.get('primary_fur_color',None)
        location = request.POST.get('location',None)
        specific_location = request.POST.get('specific_location',None)
        running = request.POST.get('running',False)
        chasing = request.POST.get('chasing',False)
        climbing = request.POST.get('climbing',False)
        eating = request.POST.get('eating',False)
        foraging = request.POST.get('foraging',False)
        other_activities = request.POST.get('other_activities',None)
        kuks = request.POST.get('kuks',False)
        quaas = request.POST.get('quaas',False)
        tail_flags = request.POST.get('tail_flags',False)
        tail_twitches = request.POST.get('tail_twitches',False)
        approaches = request.POST.get('approaches',False)
        indifferent = request.POST.get('indifferent',False)
        runs_from = request.POST.get('runs_from',False)
        moans = request.POST.get('moans',False)
        have_image = request.POST.get('have_image',False)
        #save those things
        test1 = biaoge(
            xx = latitude,
            yy = longtitude,
            Unique_Squirrel_ID = Unique_Squirrel_ID,
            shift = shift,
            date =date,
            age =age,
            primary_fur_color =primary_fur_color,
            location =location,
            specific_location =specific_location,
            running =running,
            chasing =chasing,
            climbing =climbing,
            eating =eating,
            foraging =foraging,
            other_activities =other_activities,
            kuks =kuks,
            quaas =quaas,
            tail_flags =tail_flags,
            tail_twitches =tail_twitches,
            approaches =approaches,
            indifferent =indifferent,
            runs_from =runs_from,
            moans =moans,
            profile_image= request.FILES.get('profile_image',None),
            have_image =have_image,
            )
        test1.save()
        return redirect(f'/success')
    else:
        context = {'squirrels':test1,
                   'method':'POST',
                   'sssss': 'sssss.jpg'
        }
        return render(request, 'htmls/checkoutGETS.html',context)

def goodview(request,squirrel_id):
    squirrels = biaoge.objects.get(pk = squirrel_id)
    context = {'squirrels':squirrels,
               'method':'GET',
               'sssss': 'sssss.jpg'
    }
    return render(request, 'htmls/checkoutGETS.html',context)

def search(request):
    squirrel_id = request.GET.get('search')
    error_msg = ''
    try:
        squirrels = biaoge.objects.get(pk = squirrel_id)
    except:
        return render(request,'htmls/busuccess.html')
    else:
        squirrels = biaoge.objects.get(pk = squirrel_id)
        context= {'squirrels':squirrels}
        return render(request, 'htmls/checkoutGETS.html',context)