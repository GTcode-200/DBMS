from tkinter import *
from PIL import Image, ImageTk
import psycopg2
import os
from tkinter import messagebox

master = Tk()
master.geometry("3000x1000")
master.configure(bg='#666666')

f = Frame(master, padx=10, pady=10)
ff = Frame(master)
f.configure(bg="#f2c496")


def connect():
    global cur
    con=psycopg2.connect(
    host="localhost",
    database="knowledge_repo",
    user="postgres",
    password="Ganesh@123"
)
    cur = con.cursor()


a = Label(f, text='UserId:', font=('Verdana', 14, 'bold'), bg='#f2c496')
b = Label(f, text='Password:', font=('Verdana', 14, 'bold'), bg='#f2c496')
c = Entry(f, width=20, bd=4, bg='#faf5e6')
d = Entry(f, width=20, bd=4, bg='#faf5e6', show='*')

def reg():

    master.destroy()

    os.system("python register.py")


def entry():

    cmd="python Window1.py "+uname
    os.system(cmd)


def login():
    connect()
    global uname
    uname = c.get()
    pword = d.get()
    cur.execute("select user_id,pwd from USER_PERMISSION")
    var = cur.fetchall()

    if (uname == '' or pword == ''):
        messagebox.showerror("Error", "Fields cannot be empty!")
    else:
        if (int(uname), pword) in var:
            master.destroy()
            entry()
        else:
            messagebox.showerror("Oops!", "Wrong credentials!")


img = Image.open('licon.jpeg')
img = img.resize((112, 123), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
x = Label(f, image=img)



e = Button(f, text="Login", font=('Verdana', 12, 'bold'), command=login, bd=2, bg='#eddaa1')
r = Button(f,text="Register", font=('Verdana', 12, 'bold'),   bd=2, bg="#d2a679",command=reg)
g = Label(ff, text='KNOWLEDGE REPOSITORY', font=('Times', 10, 'bold'), bg='#4db4f0', fg='#f5f4f2')
ff.place(anchor="s", relx=0.5, rely=1)
f.place(anchor="c", relx=0.5, rely=0.5)
a.grid(row=0, column=1)
b.grid(row=1, column=1)
c.grid(row=0, column=2)
d.grid(row=1, column=2)
e.grid(row=2, column=2)
r.grid(row=3,column=2)
x.grid(row=0, column=0, rowspan=3)
g.grid()

mainloop()


