from tkinter import *
import os
import sys
import psycopg2

uid=sys.argv[1]
a_id=sys.argv[2]

def connect():
    global cur,con
    con=psycopg2.connect(
    host="localhost",
    database="knowledge_repo",
    user="postgres",
    password="Ganesh@123"
)
    cur = con.cursor()

connect()

def EditHistory():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x1000")
    main_screen.title("Edit History")

    '''Label(main_screen, text="User: ").pack()
    user_edit = Label(main_screen, text="user1").pack()

    Label(main_screen, text="Date of edit: ").pack()
    date_edit = Label(main_screen, text="10.10.2021").pack()

    Label(main_screen, text="Type of edit: ").pack()
    type_edit = Label(main_screen, text="Creation").pack()'''

    

    cur.execute("SELECT * FROM EDIT_HISTORY WHERE ARTICLE_ID="+a_id)
    edits=cur.fetchall()

    for i in edits:
        txt="User "+str(i[5])+" "+i[4]+" this article on "+str(i[3])+" at "+str(i[2])
        Label(text=txt).pack()
    Button(main_screen,text="Back",command=back).pack()

    main_screen.mainloop()


def back():
    main_screen.destroy()
    os.system("python Article.py "+uid+" "+a_id)
    


EditHistory()