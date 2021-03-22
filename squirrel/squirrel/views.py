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
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import View
from django.shortcuts import get_object_or_404 


def map(request):
    sighting100 = random.sample(list(biaoge.objects.all()),100)
    sighting_list = []
    for sighting in sighting100:
        sighting_list.append({'xx':sighting.xx,'yy':sighting.yy})
    context = {'sightings':sighting_list,}
    return render(request,'htmls/map.html',context)
    
def success(request):
    return render(request,'htmls/success.html')

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
               'sssss': 'sssss.jpg',
    }
    return render(request, 'htmls/checkoutGETS.html',context)

def search(request):
    squirrel_id = request.GET.get('search')
    try:
        squirrels = biaoge.objects.get(pk = squirrel_id)
    except:
        return render(request,'htmls/busuccess.html')
    else:
        squirrels = biaoge.objects.get(pk = squirrel_id)
        context= {'squirrels':squirrels,
                    'sssss':'sssss.jpg',
                    }
        return render(request, 'htmls/checkoutGETS.html',context)

def overall(request):
    squirrels = biaoge.objects.order_by('Unique_Squirrel_ID')
    context = {'squirrels':squirrels,}
    return render(request,'htmls/index2.html',context)

def stats(request):
    sights = biaoge.objects.all()
    # shift
    AM_n = sights.filter(shift='AM').count()
    PM_n = sights.filter(shift='PM').count()
    AM_pct = AM_n/(AM_n + PM_n)
    AM_pct = "{:.2%}".format(AM_pct)
    PM_pct = PM_n/(AM_n + PM_n)
    PM_pct = "{:.2%}".format(PM_pct)
    # age
    Juvenile_n = sights.filter(age='Juvenile').count()
    Adult_n = sights.filter(age='Adult').count()
    Juvenile_pct = Juvenile_n / (Juvenile_n + Adult_n)
    Juvenile_pct = "{:.2%}".format(Juvenile_pct)
    Adult_pct = Adult_n / (Juvenile_n + Adult_n)
    Adult_pct = "{:.2%}".format(Adult_pct)
    # Primary_Fur_Color
    Black_n = sights.filter(primary_fur_color='Black').count()
    Gray_n = sights.filter(primary_fur_color='Gray').count()
    Cinnamon_n = sights.filter(primary_fur_color='Cinnamon').count()
    Black_pct = Black_n / (Black_n+Gray_n+Cinnamon_n)
    Black_pct = "{:.2%}".format(Black_pct)
    Gray_pct = Gray_n / (Black_n+Gray_n+Cinnamon_n)
    Gray_pct = "{:.2%}".format(Gray_pct)
    Cinnamon_pct = Cinnamon_n / (Black_n+Gray_n+Cinnamon_n)
    Cinnamon_pct = "{:.2%}".format(Cinnamon_pct)
    # Location
    Above_Ground_n = sights.filter(location='Above Ground').count()
    Ground_Plane_n = sights.filter(location='Ground Plane').count()
    Above_Ground_pct = Above_Ground_n / (Above_Ground_n+Ground_Plane_n)
    Above_Ground_pct = "{:.2%}".format(Above_Ground_pct)
    Ground_Plane_pct = Ground_Plane_n / (Above_Ground_n+Ground_Plane_n)
    Ground_Plane_pct= "{:.2%}".format(Ground_Plane_pct)
    # Runs_From
    True_n = sights.filter(runs_from=True).count()
    False_n = sights.filter(runs_from=False).count()
    True_pct = True_n / (True_n+False_n)
    True_pct = "{:.2%}".format(True_pct)
    False_pct = False_n / (True_n+False_n)
    False_pct = "{:.2%}".format(False_pct)

    context = {
            'Total':sights.count(),
            'Shift': {'AM': AM_n,'PM': PM_n},
            'Shift_pct': {'AM': AM_pct,'PM': PM_pct},
            'Age': {'Juvenile': Juvenile_n, 'Adult': Adult_n},
            'Age_pct': {'Juvenile': Juvenile_pct, 'Adult': Adult_pct},
            'Primary_Fur_Color': {'Black':Black_n, 'Gray':Gray_n, 'Cinnamon':Cinnamon_n},
            'Primary_Fur_Color_pct': {'Black':Black_pct, 'Gray':Gray_pct, 'Cinnamon':Cinnamon_pct},
            'Location': {'Above_Ground':Above_Ground_n, 'Ground_Plane':Ground_Plane_n},
            'Location_pct': {'Above_Ground':Above_Ground_pct, 'Ground_Plane':Ground_Plane_pct},
            'Runs_From': {'True':True_n, 'False':False_n},
            'Runs_From_pct': {'True':True_pct, 'False':False_pct},
            }
    return render(request, 'htmls/stats3.html', {'context':context})