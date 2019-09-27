from django.shortcuts import render
from django.db import connections
# Create your views here.

def index(request):
    conn = connections["default"]
    query = "select * from admin_releasetypes"
    print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    release_types = {}

    for data1 in data:
        release_types[data1[0]] = {
                            'release_name': data1[1],
                            }
    print('release_types: ',release_types)

    dicti = {"key": release_types}
    return render(request, 'calendar1.html', dicti)
    