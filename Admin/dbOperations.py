import random
import string
from django.db import connections
import datetime

class Release:
    conn = ""

    def __init__(self):
        self.conn = connections["default"]

    

