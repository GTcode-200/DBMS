from tkinter import *
import os
import psycopg2
#import pymysql
from PIL import Image, ImageTk

root=Tk()
root.geometry("3000x1000")
root.configure(bg='#4db4f0')
'''i1 = Image.open("licon.jpeg")
entryback= ImageTk.PhotoImage(i1)
l2 = Label(root, image=entryback, width=2000, height=1000)
l2.place(x=1, y=2)'''


def entry():
    os.system("python entry1.py")
def connect():
    global cur,con
    con=psycopg2.connect(
    host="localhost",
    database="knowledge_repo",
    user="postgres",
    password="Ganesh@123"
)
    cur=con.cursor()
def fun():
    connect()
    cur.execute("INSERT INTO USER_PERMISSION VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(int(a1.get()),0,b1.get(),c1.get(),d1.get(),u1.get(),"user",f1.get()))
    con.commit()
    root.destroy()
    os.system("python login.py")
    #var=cur.fetchall()
def fun1():
    root.update()
    a1.delete(0, 'end')
    b1.delete(0, 'end')
    c1.delete(0, 'end')
    d1.delete(0, 'end')
    u1.delete(0, 'end')
    f1.delete(0, 'end')

root.configure(background='white')
root.geometry("3000x1000")
A=Label(root,text="Register",font = ('Verdana',24,'bold'),bg='#4db4f0')
a=Label(root,text="User Id",font = ('Verdana',24,'bold'),bg='#4db4f0')
a1=Entry(root,width=20,bd=4)
b=Label(root,text="Name",font = ('Verdana',24,'bold'),bg='#4db4f0')
b1=Entry(root,width=20,bd=4)
c=Label(root,text="Mobile No:",font = ('Verdana',24,'bold'),bg='#4db4f0')
c1=Entry(root,width=20,bd=4)
d=Label(root,text="Mail id",font = ('Verdana',24,'bold'),bg='#4db4f0')
d1=Entry(root,width=40,bd=4)
u=Label(root,text="Address",font = ('Verdana',24,'bold'),bg='#4db4f0')
u1=Entry(root,width=40,bd=4)
f=Label(root,text="Create Password",font = ('Verdana',18,'bold'),bg='#4db4f0')
f1=Entry(root,width=20,bd=4,show='#')
g = Button(root, text="Create Account",command=fun)
h=Button(root, text="Clear",command=fun1)

A.place(x=600,y=100)
a.place(x=450,y=150,width=200)
a1.place(x=670,y=150)
b.place(x=450,y=200)
b1.place(x=670,y=200)
c.place(x=450,y=250)
c1.place(x=670,y=250)
d.place(x=450,y=300)
d1.place(x=670,y=300)
u.place(x=450,y=350)
u1.place(x=670,y=350)
f.place(x=450,y=400)
f1.place(x=690,y=400)
g.place(x=650,y=450,width=150)
h.place(x=800,y=450,width=150)

#os.system("login.py")
mainloop()
