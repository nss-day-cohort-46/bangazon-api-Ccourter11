import sqlite3
from django.shortcuts import render
from bangazonapi.models import Customer
from bangazonapireports.views import Connection

def userfavorite_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT 
                    c.id,
                    c.phone_number,
                    c.address,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM
                    bangazonapi_customer c
                JOIN
                    auth_user u ON c.user_id = u.id
               """)

            dataset = db_cursor.fetchall()

            favorites_by_user = {}

            for row in dataset:
                seller = Customer()
                seller.phone_number = row["phone_number"]
                seller.address = row["address"]
                uid = row["user_id"]

                if uid in favorites_by_user:
                    favorites_by_user[uid]["sellers"].append(seller)

                else:
                    favorites_by_user[uid] = {}  
                    favorites_by_user[uid]["id"] = uid    
                    favorites_by_user[uid]["full_name"] = row["full_name"]
                    favorites_by_user[uid]["sellers"] = [seller]

        list_of_user_favorites = favorites_by_user.values()      

        template = 'users/list_with_users.html'
        context = {
            'userfavorite_list': list_of_user_favorites
        }

        return render(request, template, context)
