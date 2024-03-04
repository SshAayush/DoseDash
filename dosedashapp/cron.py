# from django_cron import CronJobBase, Schedule

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1 # every minute

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'dosedashapp.my_cron_job'    # a unique code

#     def do(self):
#         # Your task goes here
#         print("Hello, World!")
from .models import Category
import random
from datetime import datetime,timedelta

def print_hello():
    number = random.randint(0,100)
    product = Category(category_name=datetime.now())
    product.save()