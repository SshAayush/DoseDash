# from django_cron import CronJobBase, Schedule

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1 # every minute

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'dosedashapp.my_cron_job'    # a unique code

#     def do(self):
#         # Your task goes here
#         print("Hello, World!")
from models import Category, Reminder
import random
from datetime import datetime,timedelta, timezone
import logging

# used to send mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Configure logging
logging.basicConfig(filename='sendReminder.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# def print_hello():
#     number = random.randint(0,100)
#     product = Category(category_name=datetime.now())
#     product.save()
#     logging.info(f'Updated reminder date for: ')
    
#     logging.info('sendReminder method completed')



def sendReminder():
    number = random.randint(0,100)
    logging.info('sendReminder method started')
    
    reminder = Reminder.objects.all()
    threshold_date = timezone.now() - timedelta(hours=1)
    
    product = Category(category_name=datetime.now(),test = "hello")
    product.save()
    
    logging.info(f'Threshold date: {threshold_date}')
    
    sendReminder = Reminder.objects.filter(Reminder_Date__lt=threshold_date)
    logging.info(f'Reminders to send: {sendReminder}')
    
    emails = []

    for reminder in sendReminder:
        emails.append(reminder.Reminder_UserName.email)
        
        subject = "Time to Order Your Medication from DoseDash"
        html_content = render_to_string('offer_mail.html',{
                                        'fname': reminder.Reminder_UserName.first_name, 
                                        'lname': reminder.Reminder_UserName.last_name, 
                                        'email': reminder.Reminder_UserName.email,
                                        })
        from_email = 'xayush.tc@gmail.com'
        logging.info(f'Sending email to: {reminder.Reminder_UserName.email}')
        
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            [reminder.Reminder_UserName.email],
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)
        
        # Update the reminder date AND time
        reminder.Reminder_Date = timezone.now()
        reminder.save()
        logging.info(f'Updated reminder date for: {reminder.Reminder_UserName.email}')
    
    logging.info('sendReminder method completed')