from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.db.models import Q
from .models import Category, Reminder
from django.contrib.auth.models import User
from datetime import datetime,timedelta


@shared_task
def sendReminder():
    # Assuming Category and Reminder models are imported correctly
    test = Category(category_name=timezone.now(), test="mathi xa")
    test.save()
    
    reminder = Reminder.objects.all()
    threshold_date = timezone.now() - timedelta(hours=1)
    
    sendReminder = Reminder.objects.filter(Reminder_Date__lt=threshold_date)
    
    emails = []
    
    for reminder in sendReminder:
        test2 = Category(category_name=timezone.now(), test="For vitra xiryo")
        test2.save()
        
        emails.append(reminder.Reminder_UserName.email)
        
        subject = "Time to Order Your Medication from DoseDash"
        html_content = render_to_string('offer_mail.html', {
            'fname': reminder.Reminder_UserName.first_name, 
            'lname': reminder.Reminder_UserName.last_name, 
            'email': reminder.Reminder_UserName.email,
        })
        from_email = 'xayush.tc@gmail.com'
        to = [reminder.Reminder_UserName.email]

        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            to,
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)
        
        # Update the reminder date AND time
        reminder.Reminder_Date = timezone.now()
        reminder.save()
    
    test1 = Category(category_name=timezone.now(), test="aayooooo")
    test1.save()
    
    print("Reminder sent successfully.")