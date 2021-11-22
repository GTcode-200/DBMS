from tkinter import *
import os
import psycopg2
import sys
from datetime import datetime

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

def edit_content():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x1000")

    global articles
    cur.execute("SELECT * FROM ARTICLE WHERE ARTICLE_ID="+a_id)
    articles=cur.fetchone()
    
    global article_content
    Label(main_screen, text="Edit Content: ").pack()
    article_content = Text(main_screen,height=10,width=50)
    article_content.pack()
    
    article_content.insert(END,articles[4])

    Button(main_screen,text="Confirm Edit",command=confirm).pack()
    Button(main_screen,text="Back",command=back).pack()

    main_screen.mainloop()

def back():
    main_screen.destroy()
    os.system("python Article.py "+uid+" "+a_id)

def confirm():
    cur.execute("UPDATE ARTICLE SET ARTICLE_CONTENT='"+article_content.get(1.0, "end-1c")+"'")
    con.commit()
    cur.execute("SELECT * FROM EDIT_HISTORY")
    edit_rows=cur.fetchall()
    if(edit_rows):
        edit_id=edit_rows[-1][0]+1
    else:
        edit_id=1
    cur.execute("INSERT INTO EDIT_HISTORY VALUES(%s,%s,%s,%s,%s,%s)",(edit_id,a_id,datetime.now(),datetime.now(),'modified',uid))
    con.commit()
    main_screen.destroy()
    os.system("python Article.py "+uid+" "+a_id)

edit_content()

