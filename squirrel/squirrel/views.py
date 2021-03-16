from django.http import HttpResponse
import random
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from django.db.models import Sum, Count
from .models import biaoge
import csv
import os
import datetime
import json
from django.forms import ModelForm
from .forms import SquirrelForm

def main(request):
    squirrels = biaoge.objects.order_by('Unique_Squirrel_ID')
    number = biaoge.objects.count()
    context = {'squirrels':squirrels,
               'number': number,
    }

    return render(request,'htmls/main.html',context)

def map(request):
    sighting100 = random.sample(list(biaoge.objects.all()),100)
    sighting_list = []
    for sighting in sighting100:
        sighting_list.append({'xx':sighting.xx,'yy':sighting.yy})
    context = {'sightings':sighting_list,}
    return render(request,'htmls/map.html',context)

def edit(request, squirrel_id):
    squirrel = biaoge.objects.get(pk = squirrel_id)
    form = SquirrelForm(request.POST, instance = squirrel)
    context = {'form':form,}
    return render(request,'htmls/edit.html',context)

def add(request):
    form = SquirrelForm()
    context = {'form':form,}

    return render(request,'htmls/add.html',context)
def status(request, squirrel_id):
    squirrels = biaoge.objects.get(pk = squirrel_id)
    context = {'squirrel_id':squirrel_id,
                'alldata_xx' : squirrels.xx,
                'alldata_yy' : squirrels.yy,
                'alldata_Unique_Squirrel_ID' : squirrel_id,
                'alldata_shift': squirrels.shift,
                'alldata_date' : squirrels.date,
                'alldata_age' : squirrels.age,
                'alldata_primary_fur_color' : squirrels.primary_fur_color,
                'alldata_location' : squirrels.location,
                'alldata_specific_location' : squirrels.specific_location,
                'alldata_running' : squirrels.running,
                'alldata_chasing' : squirrels.chasing,
                'alldata_climbing' : squirrels.climbing,
                'alldata_eating' : squirrels.eating,
                'alldata_foraging' : squirrels.foraging,
                'alldata_other_activities' : squirrels.other_activities,
                'alldata_kuks' : squirrels.kuks,
                'alldata_quaas' : squirrels.quaas,
                'alldata_moans' : squirrels.moans,
                'alldata_tail_flags' : squirrels.tail_flags,
                'alldata_tail_twitches' : squirrels.tail_twitches,
                'alldata_approaches' : squirrels.approaches,
                'alldata_indifferent' : squirrels.indifferent,
                'alldata_runs_from' :squirrels.runs_from, 
    }
    return render(request,'htmls/stats.html',context)

    