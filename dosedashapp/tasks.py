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
    threshold_date = timezone.now() - timedelta(hours=1)
    
    #IDs of the users who have reminders older than the threshold date
    user_ids_with_reminders = Reminder.objects.filter(Reminder_Date__lt=threshold_date).values_list('Reminder_UserName_id', flat=True).distinct()
    
    #for each user get their reminders and aggregate products
    for user_id in user_ids_with_reminders:
        user_reminders = Reminder.objects.filter(Reminder_UserName_id=user_id).select_related('Reminder_UserName')
        user_email = user_reminders.first().Reminder_UserName.email
        user_first_name = user_reminders.first().Reminder_UserName.first_name
        user_last_name = user_reminders.first().Reminder_UserName.last_name
        
        # This is a placeholder to get all products for the user
        products = user_reminders.values_list('Reminder_ProductId__Product_Name', flat=True)
        
        subject = "Time to Order Your Medication from DoseDash"
        html_content = render_to_string('offer_mail.html', {
            'fname': user_first_name, 
            'lname': user_last_name, 
            'email': user_email,
            'products': list(products), # Convert to list to ensure it's iterable
        })
        from_email = 'xayush.tc@gmail.com'
        to = [user_email]

        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            to,
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)
        
        # Update the reminder date AND time for all reminders of this user
        Reminder.objects.filter(Reminder_UserName_id=user_id).update(Reminder_Date=timezone.now())
    print("Reminder sent successfully.")