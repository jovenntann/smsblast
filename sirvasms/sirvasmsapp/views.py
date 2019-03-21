from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

# Redirect to External Links
from django.shortcuts import redirect


# Login and Logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from sirvasms import settings
from django.contrib.auth.decorators import login_required

# Models
from django.db.models import Q
from django.db.models import Sum
from django.db.models import Count

from sirvasmsapp.models import Received
from sirvasmsapp.models import Queue
from sirvasmsapp.models import QueueBlast
from sirvasmsapp.models import DateRange
from sirvasmsapp.models import Rate
from sirvasmsapp.models import Contact
from sirvasmsapp.models import Prefix
from sirvasmsapp.models import Goip

from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Upload
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
import re

# For Graph 
import calendar
from datetime import timedelta, date
import datetime
from collections import OrderedDict

# GoIP Gateway
import requests
import json
import pprint
import re

# Math
import math

# AJAX
from django.http import JsonResponse

# Export to CSV
import csv

def queue_message(tag,filename,request):

    df = pd.read_excel('/opt/djangoprojects/sirvasms/media/' + filename, sheet_name='Sheet1')

    current_user = request.user
    user_id = current_user.username

    for i in df.index:

        number = df['number'][i]
        content = df['content'][i]

        # Add Zero if Number is Incomplete
        if len(str(number)) == 10:
            number = '0' + str(df['number'][i])

        # Select Which Provider Based on Prefix
        if len(str(number)) < 5:
            provider = 'NONE'
        elif Prefix.objects.filter(prefix=number[:4]).exists():
            provider_get = Prefix.objects.get(prefix=number[:4])
            provider = provider_get.provider
        else:
            provider = 'NONE'

        goip = "" # GOIP VALUE
            
        user_object = Queue(provider = provider, to_number = number, user = user_id, message = content, goip = goip, tag = tag)
        user_object.save()

        # print("Number: " + str(number) + " Provider: " + provider + " Content: " + content + " Count:" + str(i))

def upload_contacts(group,filename,request):

    df = pd.read_excel('/opt/djangoprojects/sirvasms/media/' + filename, sheet_name='Sheet1')

    current_user = request.user
    user_id = current_user.username


    for i in df.index:

        # number = '0' + str(df['number'][i])
        name = df['name'][i]
        number = df['number'][i]

        if len(str(number)) == 10:
            number = '0' + str(df['number'][i])

        user_object = Contact(name = name, number = number, group = group)
        user_object.save()

        # print("Number: " + str(number) + " Provider: " + provider + " Content: " + content + " Count:" + str(i))


def Login(request): #login is reserved word -- strictly use Login :)
  
    if request.user.is_superuser:
        next = request.GET.get('next', '/portal/home')
    else: 
        next = request.GET.get('next', '/portal/reports')
    
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "sirvasmsapp/login.html", {'redirect_to': next})

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def index(request):
    return HttpResponseRedirect('portal/home/')
  
@login_required
def home(request):
  
    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id
    
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/home"

    sms_sent = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])&Q(flag=1))
    sms_sent = sms_sent.count()

    sms_received = Received.objects.filter(Q(date__range=[date_from, date_to]))
    sms_received = sms_received.count()

    sms_queue = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])&Q(flag=0))
    sms_queue = sms_queue.count()

    sms_failed = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])&Q(flag=2))
    sms_failed = sms_failed.count()

    # GOIP LISTS
    goip_lists = Goip.objects.filter()

    # sent_sell = Email.objects.filter(Q(date__range=[date_from, date_to])).order_by('id').aggregate(Sum('sell'))
    # sent_sell = sent_sell['sell__sum']

    # received_buy = SMS.objects.filter(Q(date__range=[date_from, date_to])).order_by('id').aggregate(Sum('buy'))
    # received_buy = received_buy['buy__sum']

    # received_sell = SMS.objects.filter(Q(date__range=[date_from, date_to])).order_by('id').aggregate(Sum('sell'))
    # received_sell = received_sell['sell__sum']

    # getcontext().prec = 6

    # total_buy = Decimal(sent_buy) + Decimal(received_buy)
    # total_sell = Decimal(sent_sell) + Decimal(received_sell)

    # total_earnings = Decimal(total_sell) - Decimal(total_buy)
    # total_earnings_php = Decimal(total_earnings) * Decimal(52.91)

    # # GRAPH USAGE PER COUNTRY #######################################################################################################################

    # countries = Rate.objects.all()

    # graph_list = []

    # for x in countries:

    #     total_sent = Email.objects.filter(Q(date__range=[date_from, date_to]),Q(subject__icontains=x.code)).order_by('id').aggregate(Sum('sell'))
    #     total_sent = total_sent['sell__sum']

    #     total_received = SMS.objects.filter(Q(date__range=[date_from, date_to]),Q(to_number__icontains=x.code)).order_by('id').aggregate(Sum('sell'))
    #     total_received = total_received['sell__sum']

    #     if total_sent is None:
    #         total_sent = 0.0000

    #     if total_received is None:
    #         total_received = 0.0000

    #     graph_dict = {'country':x,'total_sent':total_sent,'total_received':total_received}
    #     graph_list.append(dict(graph_dict))
        
        
    # # GRAPH LAST 30 DAYS ##############################################################################################################################   

    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)
        
    start_date = date(int(daterange_get.date_from.strftime("%Y")), int(daterange_get.date_from.strftime("%m")), int(daterange_get.date_from.strftime("%d")))
    end_date = date(int(daterange_get.date_to.strftime("%Y")), int(daterange_get.date_to.strftime("%m")), int(daterange_get.date_to.strftime("%d")))

    graph_date_list = []
    graph_date_dict = {}

    for single_date in daterange(start_date, end_date):
                    
        total_sent = Queue.objects.filter(Q(flag=1),Q(dateSent__range=[single_date, single_date + timedelta(days=1)])).order_by('id').count()
        total_received = Received.objects.filter(Q(date__range=[single_date, single_date + timedelta(days=1)])).order_by('id').count()
        
        if total_sent is None:
            total_sent = 0
            
        if total_received is None:
            total_received = 0

        graph_date_dict = {'date':single_date.strftime("%Y-%m-%d"),'total_sent':total_sent,'total_received':total_received}
        graph_date_list.append(dict(graph_date_dict))
          
    home_context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'sms_sent':sms_sent,
        'sms_received':sms_received,
        'sms_queue':sms_queue,
        'sms_failed':sms_failed,
        'activate':'home',
        # 'graph_list':graph_list,
        'graph_date_list':graph_date_list,
        'goip_lists':goip_lists,
    }

    return render(request,'sirvasmsapp/home.html', context=home_context)
        
   
  
@login_required
def daterange_submit(request):
        
    date_from = request.POST['from']
    date_to = request.POST['to']
    current_url = request.POST['current_url']
    
    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id
    
    DateRange.objects.filter(id=user_id).update(date_from = date_from, date_to = date_to)

    return HttpResponseRedirect(current_url)
        
@login_required
def received(request):
  
    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id

    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/received/"

    received_lists = Received.objects.filter().order_by('-id')
    received_lists = Received.objects.filter(Q(date__range=[date_from, date_to])).order_by('-id')

    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'received_lists':received_lists,
        'activate':'received',
    }
    return render(request,'sirvasmsapp/received.html',context=context)
        
  
@login_required
def sent(request):
  
    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id
       
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/sent/" 

    sent_lists = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])).order_by('-dateSent')[:500]

    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'sent_lists':sent_lists,
        'activate':'sent',
    }
    return render(request,'sirvasmsapp/sent.html',context=context)

@login_required
def contacts(request):
  
    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id
       
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/contacts/" 

    group = Contact.objects.filter().values_list('group', flat=True).distinct()
    
    contacts_list = []
    contacts_dict = {}
    
    for i in group:

        count = Contact.objects.filter(group=i)
        count = count.count()

        contact_get = Contact.objects.filter(group=i)[0]
        _id = contact_get.id
        date = contact_get.date

        contacts_dict = {'id':_id,'group':str(i),'date':date,'count':count}
        contacts_list.append(dict(contacts_dict))

    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'group_list':contacts_list,
        'activate':'contacts',
    }
    return render(request,'sirvasmsapp/contacts.html',context=context)

  
@login_required
def contacts_list(request,group):

    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id
       
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/contacts/" 

    contacts_list = Contact.objects.filter(group=group).order_by('id')

    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'contacts_list':contacts_list,
        'group':group,
        'activate':'contacts',
    }

    return render(request,'sirvasmsapp/contacts_list.html',context=context)

@login_required
def queue(request):
  
    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id
       
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/sent/" 

    queue_lists = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])&Q(flag=False)).order_by('-id')[:500]

    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'queue_lists':queue_lists,
        'activate':'queue_all',
    }
    return render(request,'sirvasmsapp/queue.html',context=context)
  
@login_required
def queue_blast(request):
  
    # Get Current Logged-in User ID
    current_user = request.user
    user_id = current_user.id
       
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/sent/" 


    # queue_lists = QueueBlast.objects.filter(Q(date__range=[date_from, date_to])).order_by('-id')

    queueblast = QueueBlast.objects.filter().order_by('-id')

    queueblast_list = []
    queueblast_dict = {}
    
    for i in queueblast:

        queueblast_get = QueueBlast.objects.filter(tag=i)[0]

        _id = queueblast_get.id
        date = queueblast_get.date
        tag = queueblast_get.tag
        message = queueblast_get.message
        status = queueblast_get.status

        count_total = Queue.objects.filter(tag=tag)
        count_total = count_total.count()

        count_sent = Queue.objects.filter(Q(tag=tag)&Q(flag=2)|Q(tag=tag)&Q(flag=1))
        count_sent = count_sent.count()

        count_failed = Queue.objects.filter(Q(tag=tag)&Q(flag=2))
        count_failed = count_failed.count()

        count_success = Queue.objects.filter(Q(tag=tag)&Q(flag=1))
        count_success = count_success.count()
        
        percent = (float(count_sent)/float(count_total)) * 100.0
    
        # Set Action
        if count_total == count_success:
            action = "Done"
        elif count_total > count_success:
            action = "Resend"

        # Set Status
        if count_total == count_sent:
            status = "Finish"
        
        queueblast_dict = {'id':_id,'date':date,'tag':tag,'message':message,'total':count_total,'sent':count_sent,'failed':count_failed,'success':count_success,'percent':percent,'action':action,'status':status}
        queueblast_list.append(dict(queueblast_dict))


    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'queueblast_list':queueblast_list,
        'activate':'queue_blast',
    }
    return render(request,'sirvasmsapp/queue_blast.html',context=context)
 
@login_required
def queue_blast_resend(request,tag):

    Queue.objects.filter(Q(tag=tag)&Q(flag=2)).update(flag=0)
    return HttpResponseRedirect('/portal/queue_blast/') 


@login_required
def sendsms(request):

    number = request.POST['number']
    message = request.POST['message']

    current_user = request.user
    user_id = current_user.username
    tag = 'Direct'

    # Check if Prefix in Dtabase
    get_prefix = Prefix.objects.get(prefix=number[:4])

    # Select Which Provider
    if len(str(number)) < 5:
        provider = 'NONE'
    elif get_prefix:
        provider_get = Prefix.objects.get(prefix=number[:4])
        provider = provider_get.number
    else:
        provider = 'NONE'

    user_object = Queue(provider = provider, name = 'None', to_number = number, user = user_id, message = message, tag = tag)
    user_object.save()
      
    return HttpResponseRedirect('/portal/queue/')

@login_required
def smsblast_upload(request):

    current_user = request.user
    user_id = current_user.id
       
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/smsblast/upload/" 
    activate = 'smsblast_upload'
      
    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'activate':activate,
    }

    return render(request,'sirvasmsapp/smsblast_upload.html',context=context)
      
@login_required
def smsblast_group(request):

    current_user = request.user
    user_id = current_user.id
       
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    current_url = "/portal/smsblast/upload/" 
    activate = 'smsblast_group'
    
    group = Contact.objects.filter().values_list('group', flat=True).distinct()
    group_list = []

    for i in group:
        group_list.append(str(i))

    context = {
        'current_url':current_url,
        'date_from':date_from,
        'date_to':date_to,
        'activate':activate,
        'group_list':group_list,
    }

    return render(request,'sirvasmsapp/smsblast_group.html',context=context)
      

@login_required
def smsblast_submit(request):

    
    if request.method == 'POST' and request.FILES['myfile']:

        tag = request.POST['tag']

        if tag == '':
            return HttpResponse("Please Enter Tag Name", content_type="text/plain")
        elif Queue.objects.filter(tag=tag):
            return HttpResponse("TAG name already exist. Please use different TAG name", content_type="text/plain")
        else:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)

            queue_message(tag,filename,request)

            # Save record to Queue Blast Tables
            user_object = QueueBlast(tag = tag, message = '[Message is uploaded in excel file.]', status = 'Sending')
            user_object.save()

            return HttpResponseRedirect('/portal/queue_blast/')
    
    else:
        return HttpResponse("Please Enter TAG and Attached the Excel File", content_type="text/plain")

            

@login_required
def smsblast_group_submit(request):

    current_user = request.user
    user_id = current_user.username

    if request.method == 'POST':
        tag = request.POST['tag']
        provider = request.POST['provider']
        groups = request.POST.getlist('groups[]')
        message = request.POST['message']

        for i in groups:

            contact_lists = Contact.objects.filter(group=i).order_by('id')
        
            for x in contact_lists:
                            
                # If Provider is BLASTING 
                if provider == 'BLASTING':
                    if len(str(x.number)) < 5:
                        provider = 'NONE'
                    elif Prefix.objects.filter(prefix=x.number[:4]).exists():
                        provider_get = Prefix.objects.get(prefix=x.number[:4])
                        provider = provider_get.provider
                    else:
                        provider = 'NONE'

                user_object = Queue(provider = provider, name = x.name, to_number = x.number, user = user_id, message = message, goip = "", tag = tag)
                user_object.save()

        # Save record to Queue Blast Tables
        user_object = QueueBlast(tag = tag, message = message, status = 'Sending')
        user_object.save()

    return HttpResponseRedirect('/portal/queue_blast/')

@login_required
def contacts_submit(request):

    if request.method == 'POST' and request.FILES['fileName']:

        group = request.POST['group']

        if group == '':
            return HttpResponse("Please Enter Group Name", content_type="text/plain")
        elif Contact.objects.filter(group=group):
            return HttpResponse("Group name already exist. Please use different Group name", content_type="text/plain")
        else:
            myfile = request.FILES['fileName']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)

            upload_contacts(group,filename,request)

            return HttpResponseRedirect('/portal/contacts/')

def export_received_csv(request):

    current_user = request.user
    user_id = current_user.id

    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="received.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'From', 'Name', 'Destination', 'Message', 'MessageSid', 'Status'])
    

    Inbox = Received.objects.filter(Q(date__range=[date_from, date_to])).order_by('-id').values_list('date', 'from_number', 'name', 'to_number', 'message', 'MessageSid', 'status')

    for i in Inbox:
       writer.writerow([i[0], i[1], i[2].encode('ascii', 'ignore').decode('ascii'), i[3], i[4], i[5], i[6]])

    return response

@login_required
def ajax_queue_status(request):

    current_user = request.user
    user_id = current_user.id
    
    daterange_get = DateRange.objects.get(id=user_id)
    date_from = str(daterange_get.date_from)
    date_to = str(daterange_get.date_to)

    sms_sent = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])&Q(flag=1))
    sms_sent = sms_sent.count()

    sms_received = Received.objects.filter(Q(date__range=[date_from, date_to]))
    sms_received = sms_received.count()

    sms_queue = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])&Q(flag=0))
    sms_queue = sms_queue.count()

    sms_failed = Queue.objects.filter(Q(dateSent__range=[date_from, date_to])&Q(flag=2))
    sms_failed = sms_failed.count()

    json_data = {
        'sms_sent':sms_sent,'sms_received':sms_received,'sms_queue':sms_queue,'sms_failed':sms_failed,
    }

    return JsonResponse(json_data)


def error_404(request):
  return render(request,'sirvasmsapp/404.html')

def error_500(request):
  return render(request,'sirvasmsapp/505.html')