from django.core.management.base import BaseCommand, CommandError
import csv
import os
import datetime
from squirrel.models import biaoge

class Command(BaseCommand):
    help = 'Export csv files'

    def handle(self,*args,**options):