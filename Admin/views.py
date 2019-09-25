from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse


# Create your views here.

def createRelease(request):
        conn = connections["default"]
        msg = {}
        if request.method == "POST":
            # uname = request.session.get('uname')
            release_name = request.POST.get('release_name', "ReleaseTest")
            start_date = request.POST.get('start_date', "2019-09-16")
            end_date = request.POST.get("end_date", "2019-09-16")
            query = "insert into releases(release_name, start_date, end_date) values ('"+ release_name + "', " +str(start_date) +"," +str(end_date) + ")"
            print("Query is => "+ query)
            cursor = conn.cursor()
            cursor.execute(query)
            msg = {"message": "Release added succesfully"}
            return render(request, "myapp/addRelease.html", msg)
        return render(request, "myapp/addRelease.html", msg)

def CreateRelease(request):
    conn = connections["default"]
    msg = {}
    if request.method == 'POST':
        release_name = request.POST.get("release_name")
        description = request.POST.get("description")
        query = "insert into admin_releasetypes(release_name) values ('"+ release_name + "')"
        cursor = conn.cursor()
        cursor.execute(query)
        msg = {"message": "Release added succesfully"}
        return render(request, "myapp/addRelease.html", msg)


def editRelease(request):
     conn = connections["default"]

def EditRelease(request):
     conn = connections["default"]