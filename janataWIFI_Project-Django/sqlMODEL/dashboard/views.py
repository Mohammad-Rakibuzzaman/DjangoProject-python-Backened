# Write Python3 code here
from django.shortcuts import render,redirect
from http import HTTPStatus
from django.http import HttpResponse
import mysql.connector as mcdb

conn = mcdb.connect(host="127.0.0.1", user="root", passwd="rtz08", database='tbit')
print('Successfully connected to database')
cur = conn.cursor()


# Create your views here.
def Table(request):
    cur.execute("SELECT * FROM tbit.janata_data;")
    data = cur.fetchall()
    # return list(data)
    print(list(data))
    return render(request, 'table.html', {'categories': data})


def categorycreate(request):
    return render(request, 'add.html')

def categoryaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['txt1']
        cur.execute("INSERT INTO janata_data (date) VALUES ('{}')".format(catname))

        conn.commit()
        return redirect(categorycreate)
    else:
        return redirect(categorycreate)


def categorydelete(request, date):
    # id = request.GET['id']
    # id = User.objects.get(id=id)
    print(date)
    cur.execute("delete from janata_data where `date` = {}".format(date))
    conn.commit()
    return redirect(categorylisting)


# def categoryedit(request, id):
#     print(id)
#     cur.execute("select * from `tb_category` where `category_id` = {}".format(id))
#     data = cur.fetchone()
#     # return list(data)
#     print(list(data))
#     return render(request, 'edit.html', {'categories': data})
#
#
# def categoryupdate(request):
#     if request.method == 'POST':
#         print(request.POST)
#         catid = request.POST['txt1']
#         catname = request.POST['txt2']
#         cur.execute("update `tb_category` set `category_name` ='{}' where `category_id`='{}'".format(catname, catid))
#         conn.commit()
#         return redirect(categorylisting)
#     else:
#         return redirect(categorylisting)
