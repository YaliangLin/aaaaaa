from django.core.management.base import BaseCommand, CommandError
import csv
import os
import datetime
from squirrel.models import biaoge


class Command(BaseCommand):
    help = 'Import csv files'

    def handle(self,*args,**options):
        def tf(text):
            if text.lower() == 'true':
                return True
            elif text.lower() == 'false':
                return False
            else:
                return None
        path123 = "vfnx-vebw.csv"
        with open(path123,'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                alldata = biaoge()
                alldata.xx = float(row['x'])
                alldata.yy = float(row['y'])
                alldata.Unique_Squirrel_ID = row['unique_squirrel_id']
                alldata.shift = row['shift']
                alldata.date = datetime.datetime.strptime(row['date'],'%m%d%Y')
                alldata.age = row['age']
                alldata.primary_fur_color = row['primary_fur_color']
                alldata.location = row['location']
                alldata.specific_location = row['specific_location']
                alldata.running = tf(row['running'])
                alldata.chasing = tf(row['chasing'])
                alldata.climbing = tf(row['climbing'])
                alldata.eating = tf(row['eating'])
                alldata.foraging = tf(row['foraging'])
                alldata.other_activities = row['other_activities']
                alldata.kuks = tf(row['kuks'])
                alldata.quaas = tf(row['quaas'])
                alldata.moans = tf(row['moans'])
                alldata.tail_flags = tf(row['tail_flags'])
                alldata.tail_twitches = tf(row['tail_twitches'])
                alldata.approaches = tf(row['approaches'])
                alldata.indifferent = tf(row['indifferent'])
                alldata.runs_from =tf(row['runs_from'])            
                alldata.save()
            print('导入成功')