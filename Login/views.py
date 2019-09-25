from django.shortcuts import render
from django.core.mail import EmailMessage
from django.db import connections
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

import string
import random

from Login.DbOperations import Login

# Create your views here.

def list1(request):
    return render(request, 'myapp/login.html')

def getNavigationAdmin(request):
    return render(request, "myapp/navigationAdmin.html")

def logout(request):
    request.session['username'] = -1
    return render(request, "myapp/login.html", {"Error": False})

def check(request):
    if request.method == 'POST':
        l = Login()
        uname = request.POST['uname']
        upass = request.POST['upass']
        request.session['username'] = uname

        if l.checkLogin(uname, upass, request):
            return HttpResponseRedirect(reverse('calender'))
            #return render(request, "calendar1.html", {"username":uname})
        else:
            return render(request, 'myapp/login.html', {'Error': True})
    else:
        return render(request, 'myapp/login.html')



