from os import name
from django.shortcuts import render , HttpResponseRedirect
from.forms import UserForm
#import pywhatkit
import datetime
from .models import User

# Create your views here.
def add_show(request):
    fm = UserForm(request.POST)
    if request.method == 'POST' and fm.is_valid:
        
        pn = request.POST.get('phone_no', 'default')
        current_time = datetime.datetime.now()
        a = current_time.hour
        b=current_time.minute
        #pywhatkit.sendwhatmsg( str(pn), "CONGRATS! you have been registered to CRUD",  a,b )
        fm.save()
            
    else:
        fm = UserForm()
    stud= User.objects.all()
    return render (request, 'enroll/add_and_show.html', {'form': fm , 'stu':stud} )

def delete_data(request, id):
    pi= User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = UserForm(instance = pi)
    return render (request, 'enroll/update_student.html', {'form':fm})

