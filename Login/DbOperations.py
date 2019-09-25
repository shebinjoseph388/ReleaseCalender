from django.db import connections
# from Constants.const import constant

class Login:
    conn = ""

    def __init__(self):
        self.conn = connections["default"]
    
    def checkLogin(self, username, passw, request):
        query = "select username from `login_users` where username='{}' and password='{}' ".format(username, passw)
        cursor = self.conn.cursor()
        print(query)
        if cursor.execute(query):
            res = cursor.fetchone()
            request.session['id'] = res[0]
            return True
        return False